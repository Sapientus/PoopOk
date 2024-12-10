from datetime import datetime, timedelta, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import User, ToiletSession
from src.repository.toilet_session_king import update_king_stats, get_current_king, apply_king_bonus
from src.services.toilet_sessions import STARS_REWARD, MAX_TOILET_TIME, STARS_PENALTY, can_start_new_session
from src.utils.toilet_session_utils import get_active_session


async def start_toilet_session(user: User, db: AsyncSession) -> ToiletSession:
    try:
        can_start, message = await can_start_new_session(user, db)
        if not can_start:
            raise ValueError(message)

        session = ToiletSession(
            user_id=user.id,
            start_time=datetime.now(timezone.utc)
        )

        db.add(session)
        await db.commit()
        await db.refresh(session)

        return session
    except ValueError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to start session for user {user.username}") from e


async def end_toilet_session(user: User, db: AsyncSession) -> tuple[ToiletSession, int, dict | None]:
    """Завершує сесію і повертає кількість отриманих/втрачених зірок та інфо про короля параші"""
    session = await get_active_session(user.id, db)
    if not session:
        raise ValueError("No active toilet session found")

    # Завершуємо сесію як раніше
    end_time = datetime.now(timezone.utc)
    duration = int((end_time - session.start_time).total_seconds())

    session.end_time = end_time
    session.duration = duration

    # нагорода або штраф
    stars_change = STARS_REWARD if duration <= MAX_TOILET_TIME else -STARS_PENALTY
    user.stars = max(0, user.stars + stars_change)
    await update_king_stats(user.id, duration, db)

    # став користувач королем?!
    current_king = await get_current_king(db)
    king_bonus_applied = False

    if current_king and current_king["username"] == user.username:
        king_bonus_applied = await apply_king_bonus(user, db)

    await db.commit()
    await db.refresh(session)

    return session, stars_change, current_king if king_bonus_applied else None


async def get_user_session_stats(user_id: int, db: AsyncSession) -> dict:
    """Отримує статистику сесій користувача за останній тиждень"""
    week_ago = datetime.now(timezone.utc) - timedelta(days=7)

    query = select(ToiletSession).where(
        ToiletSession.user_id == user_id,
        ToiletSession.end_time >= week_ago
    )
    result = await db.execute(query)
    sessions = result.scalars().all()

    total_sessions = len(sessions)
    sessions_within_limit = sum(1 for s in sessions if s.duration and s.duration <= MAX_TOILET_TIME)
    total_time = sum((s.duration or 0) for s in sessions)

    return {
        "total_sessions": total_sessions,
        "sessions_within_limit": sessions_within_limit,
        "success_rate": round(sessions_within_limit / total_sessions * 100 if total_sessions > 0 else 0, 2),
        "total_time": total_time,
        "average_time": round(total_time / total_sessions if total_sessions > 0 else 0, 2)
    }
