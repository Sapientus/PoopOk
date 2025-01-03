from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.entity.models import User
from src.i18n.translations import translator
from src.schemas.user import UserResponseAboutMe
from src.services.auth import auth_service
from src.services.cloud_service import CloudService
from src.repository import users as repositories_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/mystats", response_model=UserResponseAboutMe)
async def get_current_user(user: User = Depends(auth_service.get_current_user)):
    return user


@router.get("/{username}", response_model=UserResponseAboutMe, description="Пошук за нікнеймом")
async def get_user_profile(username: str, current_user: User = Depends(auth_service.get_current_user),
                           db: AsyncSession = Depends(get_db), t: callable = Depends(translator)):
    user_profile = await repositories_users.get_user_by_username(username, db)
    if username.lower() == current_user.username.lower():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=t("user.own_profile_error")
        )
    if not user_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=t("user.not_found"))
    return user_profile


@router.patch("/avatar", response_model=UserResponseAboutMe)
async def update_avatar(
        file: UploadFile = File(),
        user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db),
        request: Request = None
):
    """Update user's avatar by uploading it to Cloudinary and updating the database."""
    if request is None:
        request = Request(scope={"type": "http"})  # Provide default request object if none is provided

    try:
        cloud_service = CloudService()
        # Let CloudService handle all validations
        upload_result = await cloud_service.upload_avatar(file, user.email, request)

        # Update user's avatar URL in database
        user = await repositories_users.update_avatar_url(user.email, upload_result["url"], db)

        return user
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        CloudService.handle_exceptions(e, request)
