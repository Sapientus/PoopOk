from fastapi import Depends, HTTPException, APIRouter, status, BackgroundTasks, Request
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from src.database.db import get_db
from src.schemas.user import UserSchema, TokenSchema, RequestEmail, UserBasicInfoSchema, RefreshTokenSchema
from src.repository import users as repositories_users
from src.services.auth import auth_service, password_service
from src.services.email import send_email, send_reset_password_email

router = APIRouter(prefix='/auth', tags=['Authentication'])
get_refresh_token = HTTPBearer()


@router.post("/signup", response_model=UserBasicInfoSchema, status_code=status.HTTP_201_CREATED,
             description="Реєстрація.")
async def signup(body: UserSchema, bt: BackgroundTasks, request: Request, db: AsyncSession = Depends(get_db)):
    exist_user = await repositories_users.get_user_by_email(body.email, db)

    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    body.password = password_service.get_password_hash(body.password)
    new_user = await repositories_users.create_user(body, db)
    bt.add_task(send_email, new_user.email, new_user.username, str(request.base_url))
    return new_user


@router.post("/login", response_model=TokenSchema,
             description="Отримаємо рефреш та ексес токени, але перед тим потрібно отримати confirm через "
                         "confirmed_email, токен приходить на електронну пошту при реєстрації.")
async def login(body: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await repositories_users.get_user_by_email(body.username, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not user.confirmed:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed")
    if not password_service.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    # Generate JWT
    access_token = await auth_service.create_access_token(data={"sub": user.email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": user.email})
    await repositories_users.update_token(user, refresh_token, db)

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "stars": user.stars,
        "armor": user.armor,
        "is_frozen_until": user.is_frozen_until,
        "confirmed": user.confirmed,
        "created_at": user.created_at,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.get('/refresh_token')
async def refresh_token(
        credentials: HTTPAuthorizationCredentials = Depends(get_refresh_token),
        db: AsyncSession = Depends(get_db)
) -> JSONResponse:
    """
    Endpoint to refresh access token using refresh token
    """
    try:
        token = credentials.credentials
        if not token:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "No refresh token provided"}
            )

        try:
            # Явно вказуємо, що очікуємо refresh_token
            email = await auth_service.decode_refresh_token(token)
        except HTTPException as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": f"Invalid refresh token: {str(e.detail)}"}
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": f"Token validation failed: {str(e)}"}
            )

        # Перевіряємо користувача та його refresh_token
        user = await repositories_users.get_user_by_email(email, db)
        if not user:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "User not found"}
            )

        if user.refresh_token != token:
            await repositories_users.update_token(user, None, db)
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Stored refresh token does not match provided token"}
            )

        # Генеруємо нові токени
        access_token = await auth_service.create_access_token(data={"sub": email})
        refresh_token = await auth_service.create_refresh_token(data={"sub": email})

        # Оновлюємо refresh_token в базі даних
        await repositories_users.update_token(user, refresh_token, db)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": f"Token refresh failed: {str(e)}"}
        )


@router.get('/confirmed_email/{token}',
            description="Після реєстрації токен з ел.пошти вставляємо сюди щоб отримати confirmed = True.")
async def confirmed_email(token: str, db: AsyncSession = Depends(get_db)):
    email = await auth_service.get_email_from_token(token)
    user = await repositories_users.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    await repositories_users.confirmed_email(email, db)
    return {"message": "Email confirmed"}


@router.post('/request_email', description="Для повторного відправлення з підтвердженням та токеном.")
async def request_email(body: RequestEmail, background_tasks: BackgroundTasks, request: Request,
                        db: AsyncSession = Depends(get_db)):
    user = await repositories_users.get_user_by_email(body.email, db)

    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    if user:
        background_tasks.add_task(send_email, user.email, user.username, str(request.base_url))
    return {"message": "Check your email for confirmation."}


@router.post('/request_password_reset')
async def request_password_reset(body: RequestEmail, background_tasks: BackgroundTasks,
                                 db: AsyncSession = Depends(get_db)):
    user = await repositories_users.get_user_by_email(body.email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    token = auth_service.create_password_reset_token(user.email)

    background_tasks.add_task(send_reset_password_email, user.email, user.username, token)

    return {"message": "Password reset email sent. Please check your email."}


@router.post('/reset_password/{token}', description="Пропихуємо токен з емейлу")
async def reset_password(token: str, new_password: str, db: AsyncSession = Depends(get_db)):
    email = await auth_service.verify_password_reset_token(token)
    user = await repositories_users.get_user_by_email(email, db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    hashed_password = password_service.get_password_hash(new_password)
    user.password = hashed_password
    await db.commit()

    return {"message": "Password updated successfully"}
