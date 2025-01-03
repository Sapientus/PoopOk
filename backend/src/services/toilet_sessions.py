from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import ToiletSession, User
from src.utils.toilet_session_utils import get_active_session, had_recent_session

MAX_TOILET_TIME = 900  # 15 minutes
STARS_REWARD = 3  # bonus
STARS_PENALTY = 1  # alarm


async def is_session_within_limit(session: ToiletSession) -> bool:
    """Перевіряє чи сесія вкладається в ліміт часу"""
    if not session.duration:
        return False
    return session.duration <= MAX_TOILET_TIME  # type: ignore


async def can_start_new_session(user: User, db: AsyncSession, t: callable) -> tuple[bool, str]:
    """Перевіряє чи може користувач почати нову сесію"""
    # Перевіряємо чи немає активної сесії
    active_session = await get_active_session(user.id, db)
    if active_session:
        return False, t("toilet.errors.active_session_exists")

    # Перевіряємо чи не були какульки протягом останньої години
    else:
        recent_session = await had_recent_session(user.id, db, STARS_PENALTY)

    if recent_session:
        return False, t("toilet.errors.recent_session_exists")

    return True, "OK"


async def is_user_frozen(user: User) -> bool:
    """Перевіряє, чи заморожений користувач"""
    return user.is_frozen_until is not None and user.is_frozen_until > datetime.now(timezone.utc)
