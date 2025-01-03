from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from src.database.db import get_db
from src.entity.models import User
from src.i18n.translations import translator
from src.repository.toilet_session_king import get_current_king, king_leaderboard
from src.repository.toilet_session import start_toilet_session, end_toilet_session, get_user_session_stats
from src.schemas.schemas_yeti import YetiStatusResponse
from src.schemas.toilet_session_time import (
    ToiletSessionStart,
    ToiletSessionEnd,
    ToiletSessionResponse,
    ToiletSessionEndResponse,
    UserSessionStats
)
from src.services.auth import auth_service
from src.services.status_yeti import get_most_attacked_users

router = APIRouter(prefix='/toilet-sessions', tags=['Toilet Sessions'])


@router.post("/start", response_model=ToiletSessionResponse,
             description="Перевіряємо чи може користувач почати нову сесію")
async def start_session(
        _: ToiletSessionStart,
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db),
        t: callable = Depends(translator)
):
    try:
        session = await start_toilet_session(current_user, db, t)
        return session
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=t("common.errors.internal_error")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=t("common.errors.unexpected_error").format(e=e)
        )


@router.post("/end", response_model=ToiletSessionEndResponse,
             description="Завершує сесію і повертає кількість отриманих/втрачених зірок та інфо про короля параші")
async def end_session(
        _: ToiletSessionEnd,
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db),
        t: callable = Depends(translator)
):
    try:
        session, stars_change, king_info = await end_toilet_session(current_user, db, t)  # king_info
        message = (
            t("toilet.success.stars_earned").format(stars=stars_change)
            if stars_change > 0 else
            t("toilet.success.stars_lost").format(stars=abs(stars_change))
        )
        return ToiletSessionEndResponse(
            session=session,
            stars_change=stars_change,
            king_info=king_info,
            message=message
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/stats", response_model=UserSessionStats,
            description="Отримує статистику сесій користувача за останній тиждень")
async def get_stats(
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db)
):
    return await get_user_session_stats(current_user.id, db)


@router.get("/current", description="Отримання інформації про поточного короля")
async def get_current_toilet_king(db: AsyncSession = Depends(get_db), t: callable = Depends(translator)):
    king = await get_current_king(db)
    if not king:
        raise HTTPException(
            status_code=404,
            detail=t("toilet.errors.no_current_king")
        )
    return king


@router.get("/leaderboard", description="Отримання лідерборду королів за вказаний період")
async def get_kings_leaderboard(days: int = 7, db: AsyncSession = Depends(get_db)):
    return await king_leaderboard(days, db)


@router.get("/most-attacked", response_model=list[YetiStatusResponse],
            description="Отримати список найбільш атакованих користувачів (потенційних йеті)")
async def get_yeti_status(db: AsyncSession = Depends(get_db)):
    users = await get_most_attacked_users(db)

    return [
        YetiStatusResponse(
            username=user.username,
            attack_count=attack_count,
            is_frozen=user.is_frozen_until is not None and user.is_frozen_until > datetime.now(timezone.utc),
            frozen_until=user.is_frozen_until
        )
        for user, attack_count in users
    ]
