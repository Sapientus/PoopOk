from enum import Enum
from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import User, UserAchievement, ToiletSession, PoopAttack, YetiCurseRemoval
from src.services.toilet_sessions import MAX_TOILET_TIME


class AchievementType(Enum):
    TOILET_MASTER = "toilet_master"  # За 100 успішних какульок
    POOP_WARRIOR = "poop_warrior"  # За 50 успішних атак
    ARMOR_KING = "armor_king"  # За максимальну броню
    STAR_COLLECTOR = "star_collector"  # За накопичення 100 зірок
    CURSE_BREAKER = "curse_breaker"  # За зняття 5 проклять


class AchievementReward:
    REWARDS = {
        AchievementType.TOILET_MASTER: {"stars": 20, "armor": 5},
        AchievementType.POOP_WARRIOR: {"stars": 15, "armor": 3},
        AchievementType.ARMOR_KING: {"stars": 25, "armor": 7},
        AchievementType.STAR_COLLECTOR: {"stars": 30, "armor": 4},
        AchievementType.CURSE_BREAKER: {"stars": 35, "armor": 6}
    }


async def check_achievement_conditions(user: User, achievement_type: AchievementType, db: AsyncSession) -> bool:
    """Перевіряє чи виконані умови для отримання досягнення"""
    if achievement_type == AchievementType.TOILET_MASTER:
        # Перевірка кількості успішних походеньок
        query = select(func.count(ToiletSession.id)).where(
            ToiletSession.user_id == user.id,
            ToiletSession.duration <= MAX_TOILET_TIME
        )
        result = await db.execute(query)
        return result.scalar_one() >= 100

    elif achievement_type == AchievementType.POOP_WARRIOR:
        # Перевірка кількості успішних атак
        query = select(func.count(PoopAttack.id)).where(
            PoopAttack.attacker_id == user.id
        )
        result = await db.execute(query)
        return result.scalar_one() >= 50

    elif achievement_type == AchievementType.ARMOR_KING:
        # Перевірка досягнення максимальної броні
        return user.armor == user.max_armor

    elif achievement_type == AchievementType.STAR_COLLECTOR:
        # Перевірка накопичення зірок
        return user.stars >= 100

    elif achievement_type == AchievementType.CURSE_BREAKER:
        # Перевірка кількості знятих проклять
        query = select(func.count(YetiCurseRemoval.id)).where(
            YetiCurseRemoval.user_id == user.id
        )
        result = await db.execute(query)
        return result.scalar_one() >= 5

    return False


async def grant_achievement(user: User, achievement_type: AchievementType, db: AsyncSession, t: callable):
    """Видає досягнення користувачу та нараховує нагороду"""
    # Перевіряємо чи нема вже цього досягнення
    query = select(UserAchievement).where(
        UserAchievement.user_id == user.id,
        UserAchievement.achievement_type == achievement_type.value
    )

    result = await db.execute(query)
    if result.scalar_one_or_none():
        return False, t("achievements.info.already_earned")

    # Створюємо запис про досягнення
    achievement = UserAchievement(
        user_id=user.id,
        achievement_type=achievement_type.value,
        earned_at=datetime.utcnow()
    )

    # Нараховуємо нагороду
    reward = AchievementReward.REWARDS[achievement_type]
    user.stars += reward["stars"]
    user.armor = min(user.armor + reward["armor"], user.max_armor)

    db.add(achievement)
    await db.commit()
    return True, {
        "type": achievement_type.value,
        "name": t(f"achievements.types.{achievement_type.value}.name"),
        "description": t(f"achievements.types.{achievement_type.value}.description"),
        "rewards": {
            "stars": {
                "count": reward["stars"],
                "message": t("achievements.rewards.stars_earned").format(count=reward["stars"])
            },
            "armor": {
                "count": reward["armor"],
                "message": t("achievements.rewards.armor_earned").format(count=reward["armor"])
            }
        }
    }


async def process_achievements(user: User, db: AsyncSession, t: callable):
    """Перевіряє та видає всі доступні досягнення"""
    results = []
    for achievement_type in AchievementType:
        if await check_achievement_conditions(user, achievement_type, db):
            success, result = await grant_achievement(user, achievement_type, db, t)
            if success:
                results.append(result)
    return results


async def fetch_user_achievements(user: User, db: AsyncSession, t: callable):
    """Отримує всі досягнення користувача"""
    query = select(UserAchievement).where(
        UserAchievement.user_id == user.id
    ).order_by(UserAchievement.earned_at.desc())

    result = await db.execute(query)
    achievements = result.scalars().all()

    if not achievements:
        return {
            "message": t("achievements.info.no_achievements")
        }

    return [
        {
            "type": achievement.achievement_type,
            "earned_at": achievement.earned_at,
            "rewards": AchievementReward.REWARDS[AchievementType(achievement.achievement_type)]
        }
        for achievement in achievements
    ]
