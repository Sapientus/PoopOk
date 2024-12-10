from datetime import datetime, timedelta, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import ToiletKing, User


async def update_king_stats(user_id: int, session_duration: int, db: AsyncSession) -> ToiletKing:
    """Оновлює статистику для визначення короля"""
    today = datetime.now(timezone.utc).date()

    # Отримуємо або створюємо запис за сьогодні
    query = select(ToiletKing).where(ToiletKing.user_id == user_id, ToiletKing.date == today)
    result = await db.execute(query)
    king_stats = result.scalar_one_or_none()

    if not king_stats:
        king_stats = ToiletKing(
            user_id=user_id,
            date=today,
            total_duration=session_duration,
            total_sessions=1
        )
        db.add(king_stats)
    else:
        king_stats.total_duration += session_duration
        king_stats.total_sessions += 1

    await db.commit()
    return king_stats


async def get_current_king(db: AsyncSession) -> dict | None:
    """Отримує поточного короля"""
    today = datetime.now(timezone.utc).date()

    query = select(ToiletKing, User.username).join(User).where(ToiletKing.date == today).order_by(
        ToiletKing.total_duration.desc())

    result = await db.execute(query)
    king_record = result.first()

    if not king_record:
        return None

    king_stats, username = king_record
    return {
        "username": username,
        "total_duration": king_stats.total_duration,
        "total_sessions": king_stats.total_sessions,
        "date": king_stats.date
    }


async def apply_king_bonus(user: User, db: AsyncSession):
    """Додає бонусну броню королю"""
    today = datetime.now(timezone.utc).date()

    king_stats = await db.execute(
        select(ToiletKing).where(
            ToiletKing.user_id == user.id,
            ToiletKing.date == today,
            ToiletKing.armor_bonus_applied == False
        )
    )
    king_stats = king_stats.scalar_one_or_none()

    if king_stats and not king_stats.armor_bonus_applied:
        user.armor = min(user.armor + 5, user.max_armor)  # + 5 броні
        king_stats.armor_bonus_applied = True
        await db.commit()
        return True
    return False


async def king_leaderboard(days: int, db: AsyncSession):
    start_date = datetime.now(timezone.utc).date() - timedelta(days=days)

    query = select(ToiletKing, User.username).join(User).where(ToiletKing.date >= start_date).order_by(
        ToiletKing.date.desc(), ToiletKing.total_duration.desc())

    result = await db.execute(query)
    leaders = result.all()
    return {
        "period_days": days,
        "leaders": [
            {
                "date": stats.date,
                "username": username,
                "total_duration": stats.total_duration,
                "total_sessions": stats.total_sessions
            }
            for stats, username in leaders
        ]
    }
