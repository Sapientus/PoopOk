from datetime import datetime, timedelta
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import PoopAttack, User

YETI_THRESHOLD = 5  # Кількість атак, після якої користувач стає йеті
FREEZE_DURATION = timedelta(days=2)  # Тривалість заморозки


async def check_yeti_status(target_id: int, db: AsyncSession) -> tuple[bool, datetime | None]:
    """
    Перевіряє чи користувач має стати йеті
    Повертає: (чи стати йеті, час заморозки)
    """
    # Рахуємо кількість атак за останні 24 години
    yesterday = datetime.utcnow() - timedelta(days=1)

    query = select(func.count(PoopAttack.id)).where(
        PoopAttack.target_id == target_id,
        PoopAttack.created_at >= yesterday
    )

    result = await db.execute(query)
    attack_count = result.scalar_one()

    if attack_count >= YETI_THRESHOLD:
        freeze_until = datetime.utcnow() + FREEZE_DURATION
        return True, freeze_until

    return False, None


async def update_user_yeti_status(user: User, freeze_until: datetime | None, db: AsyncSession):
    """Оновлює статус заморозки користувача"""
    user.is_frozen_until = freeze_until
    await db.commit()


async def get_most_attacked_users(db: AsyncSession, limit: int = 5) -> list[dict]:
    """Отримує список найбільш атакованих користувачів"""
    yesterday = datetime.utcnow() - timedelta(days=1)

    query = select(User, func.count(PoopAttack.id).label('attack_count')).join(PoopAttack,
                                                                               User.id == PoopAttack.target_id).where(
        PoopAttack.created_at >= yesterday).group_by(User.id).order_by(func.count(PoopAttack.id).desc()).limit(limit)

    result = await db.execute(query)
    return result.all()
