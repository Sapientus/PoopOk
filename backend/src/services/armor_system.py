from datetime import datetime, timedelta, timezone
from enum import Enum

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import User, ArmorBonus


class ArmorType(Enum):
    BASIC = "basic"  # Базова броня
    ROYAL = "royal"  # Броня короля
    LEGENDARY = "legendary"  # Легендарна броня (за особливі досягнення)


class ArmorReward:
    BASIC_MAX = 10
    ROYAL_BONUS = 5
    LEGENDARY_BONUS = 15

    @staticmethod
    def get_max_armor(armor_type: ArmorType) -> int:
        if armor_type == ArmorType.LEGENDARY:
            return ArmorReward.BASIC_MAX + ArmorReward.LEGENDARY_BONUS
        elif armor_type == ArmorType.ROYAL:
            return ArmorReward.BASIC_MAX + ArmorReward.ROYAL_BONUS
        return ArmorReward.BASIC_MAX


async def update_user_armor(user: User, armor_type: ArmorType, db: AsyncSession):
    """Оновлює тип броні користувача та її максимальне значення"""
    user.armor_type = armor_type.value
    user.max_armor = ArmorReward.get_max_armor(armor_type)

    # Якщо поточна броня перевищує новий максимум - зменшуємо її
    if user.armor > user.max_armor:
        user.armor = user.max_armor

    await db.commit()


async def apply_armor_bonus(user: User, bonus_amount: int, duration: timedelta, db: AsyncSession):
    """Додає тимчасовий бонус до броні"""
    expires_at = datetime.now(timezone.utc) + duration

    bonus = ArmorBonus(
        user_id=user.id,
        bonus_amount=bonus_amount,
        expires_at=expires_at
    )

    user.armor = min(user.armor + bonus_amount, user.max_armor)

    db.add(bonus)
    await db.commit()
    return bonus


async def check_and_remove_expired_bonuses(user: User, db: AsyncSession):
    """Перевіряє та видаляє прострочені бонуси броні"""
    query = select(ArmorBonus).where(
        ArmorBonus.user_id == user.id,
        ArmorBonus.expires_at <= datetime.now(timezone.utc),
        ArmorBonus.is_active == True
    )

    result = await db.execute(query)
    expired_bonuses = result.scalars().all()

    for bonus in expired_bonuses:
        user.armor = max(0, user.armor - bonus.bonus_amount)
        bonus.is_active = False

    await db.commit()
    return expired_bonuses


async def get_current_armor_status(user: User, db: AsyncSession) -> dict:
    """Отримує поточний статус броні користувача"""
    await check_and_remove_expired_bonuses(user, db)

    query = select(ArmorBonus).where(
        ArmorBonus.user_id == user.id,
        ArmorBonus.is_active == True
    )

    result = await db.execute(query)
    active_bonuses = result.scalars().all()

    return {
        "current_armor": user.armor,
        "max_armor": user.max_armor,
        "armor_type": user.armor_type,
        "active_bonuses": [
            {
                "amount": bonus.bonus_amount,
                "expires_at": bonus.expires_at
            } for bonus in active_bonuses
        ]
    }
