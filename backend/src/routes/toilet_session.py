from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from src.database.db import get_db
from src.entity.models import User
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
        db: AsyncSession = Depends(get_db)
):
    try:
        session = await start_toilet_session(current_user, db)
        return session
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except RuntimeError as e:
        # Наприклад, логування і підняття зрозумілої помилки для клієнта
        print(f"Runtime error in start_session: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred while starting a session."
        )
    except Exception as e:
        # Загальний випадок для неочікуваних винятків
        print(f"Unhandled exception in start_session: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )


@router.post("/end", response_model=ToiletSessionEndResponse,
             description="Завершує сесію і повертає кількість отриманих/втрачених зірок та інфо про короля параші")
async def end_session(
        _: ToiletSessionEnd,
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db)
):
    try:
        session, stars_change, king_info = await end_toilet_session(current_user, db)  # king_info
        message = (
            f"Session ended successfully! You earned {stars_change} stars for staying within the time limit!"
            if stars_change > 0 else
            f"Session ended. You lost {abs(stars_change)} stars for exceeding the time limit."
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
async def get_current_toilet_king(db: AsyncSession = Depends(get_db)):
    king = await get_current_king(db)
    if not king:
        raise HTTPException(
            status_code=404,
            detail="No toilet king for today yet"
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
