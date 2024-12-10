from datetime import datetime, timedelta
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import User, YetiCurseRemoval


class CurseRemovalCost:
    BASE_STARS = 10  # Базова вартість зняття прокляття
    ADDITIONAL_PER_DAY = 5  # Додаткова вартість за кожен день прокляття
    DEFAULT_FREEZE_DURATION = timedelta(days=3)


async def apply_yeti_curse(target: User, db: AsyncSession, duration: timedelta | None = None):
    freeze_duration = duration or CurseRemovalCost.DEFAULT_FREEZE_DURATION
    target.is_frozen_until = datetime.utcnow() + freeze_duration
    await db.commit()
    return target.is_frozen_until


async def calculate_curse_removal_cost(user: User) -> int:
    """Розраховує вартість зняття прокляття в зірках"""
    if not user.is_frozen_until:
        return 0

    days_cursed = (user.is_frozen_until - datetime.utcnow()).days
    return CurseRemovalCost.BASE_STARS + (days_cursed * CurseRemovalCost.ADDITIONAL_PER_DAY)


async def can_remove_curse(user: User) -> tuple[bool, str]:
    """Перевіряє чи може користувач зняти прокляття"""
    if not user.is_frozen_until:
        return False, "User is not cursed"

    cost = await calculate_curse_removal_cost(user)
    if user.stars < cost:
        return False, f"Not enough stars. Required: {cost}"

    return True, "OK"


async def remove_yeti(user: User, db: AsyncSession) -> tuple[bool, str, int]:
    """
    Знімає прокляття з користувача за зірки
    Повертає: (успіх, повідомлення, вартість)
    """
    can_remove, message = await can_remove_curse(user)
    if not can_remove:
        return False, message, 0

    cost = await calculate_curse_removal_cost(user)

    # Знімаємо прокляття
    user.is_frozen_until = None
    user.stars -= cost

    # Записуємо історію зняття прокляття
    removal = YetiCurseRemoval(
        user_id=user.id,
        stars_spent=cost,
        removed_at=datetime.utcnow()
    )

    db.add(removal)
    await db.commit()

    return True, "Curse removed successfully", cost


async def get_curse_history(user_id: int, db: AsyncSession, limit: int = 5):
    """Отримує історію зняття проклять користувача"""
    query = select(YetiCurseRemoval).where(
        YetiCurseRemoval.user_id == user_id
    ).order_by(YetiCurseRemoval.removed_at.desc()).limit(limit)

    result = await db.execute(query)
    return result.scalars().all()


async def applied_curse(target_user_id: int, db: AsyncSession):
    query = select(User).where(User.id == target_user_id)
    result = await db.execute(query)
    target = result.scalar_one_or_none()
    return target
