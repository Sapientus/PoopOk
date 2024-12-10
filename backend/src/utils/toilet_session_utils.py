from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import ToiletSession


async def get_active_session(user_id: int, db: AsyncSession) -> ToiletSession | None:
    """Перевіряємо чи є активна сесія"""
    query = select(ToiletSession).where(ToiletSession.user_id == user_id, ToiletSession.end_time.is_(None))
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def had_recent_session(user_id: int, db: AsyncSession, interval_hours) -> bool:  # test refactoring
    """Перевіряє чи була сесія протягом заданого часу."""
    query = select(ToiletSession).where(ToiletSession.user_id == user_id,
                                        ToiletSession.end_time >= datetime.now(timezone.utc) - timedelta(
                                            hours=interval_hours))
    result = await db.execute(query)
    return result.scalar_one_or_none() is not None
