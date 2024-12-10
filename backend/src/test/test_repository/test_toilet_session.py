import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, AsyncMock
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import User, ToiletSession
from src.repository.toilet_session import start_toilet_session, end_toilet_session, get_user_session_stats
from src.services.toilet_sessions import STARS_REWARD, STARS_PENALTY
from src.utils.toilet_session_utils import get_active_session


@pytest.fixture
async def db():
    """Mock для AsyncSession"""
    mock_db = Mock(spec=AsyncSession)
    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()
    return mock_db


@pytest.fixture
def user():
    """Фікстура для створення тестового користувача"""
    return User(
        id=1,
        username="test_user",
        stars=10
    )


class TestStartToiletSession:
    @pytest.mark.asyncio
    async def test_start_session_success(self, user, db):
        # Мокаємо `get_active_session`, щоб повертало `None` (немає активної сесії)
        with patch('src.utils.toilet_session_utils.get_active_session', AsyncMock(return_value=None)), \
                patch('src.services.toilet_sessions.can_start_new_session', return_value=(True, "OK")):
            # Налаштовуємо методи `db`
            db.execute = AsyncMock(return_value=Mock(scalar_one_or_none=lambda: None))
            db.commit = AsyncMock(return_value=None)
            db.refresh = AsyncMock(return_value=None)
            db.add = Mock()

            # Викликаємо тестовану функцію
            session = await start_toilet_session(user, db)

            # Перевіряємо результат
            assert session is not None
            assert session.user_id == user.id
            db.add.assert_called_once_with(session)  # Перевіряємо, що `db.add` викликано
            db.commit.assert_called_once()  # Перевіряємо, що `commit` викликано
            db.refresh.assert_called_once_with(session)  # Перевіряємо, що `refresh` викликано

    @pytest.mark.asyncio
    async def test_start_session_cannot_start(self, user, db):
        # Попередній варіант тесту залишається без змін
        error_message = "Cannot start new session"
        with patch('src.services.toilet_sessions.can_start_new_session', return_value=(False, error_message)):
            with pytest.raises(ValueError) as exc_info:
                await start_toilet_session(user, db)
            assert str(exc_info.value) == error_message


class TestEndToiletSession:
    @pytest.mark.asyncio
    async def test_end_session_no_active_session(self, user, db):
        """Test ending a session with no active session"""
        with patch('src.utils.toilet_session_utils.get_active_session', AsyncMock(return_value=None)):
            with pytest.raises(ValueError) as exc_info:
                await end_toilet_session(user, db)
            assert str(exc_info.value) == "No active toilet session found"

    @pytest.mark.asyncio
    async def test_end_session_success_with_reward(self, user, db):
        """Test successfully ending a session with a reward"""
        start_time = datetime.utcnow() - timedelta(minutes=4)
        session = ToiletSession(
            id=1,
            user_id=user.id,
            start_time=start_time
        )

        with patch('src.utils.toilet_session_utils.get_active_session', AsyncMock(return_value=session)), \
                patch('src.repository.toilet_king.update_king_stats', AsyncMock()), \
                patch('src.repository.toilet_king.get_current_king', AsyncMock(return_value=None)):
            result_session, stars_change, king_info = await end_toilet_session(user, db)

            assert result_session.end_time is not None
            assert result_session.duration is not None
            assert stars_change == STARS_REWARD
            assert king_info is None
            db.commit.assert_called_once()
            db.refresh.assert_called_once_with(result_session)

    @pytest.mark.asyncio
    async def test_end_session_with_penalty(self, user, db):
        """Test ending a session with a penalty"""
        start_time = datetime.utcnow() - timedelta(minutes=15)
        session = ToiletSession(
            id=1,
            user_id=user.id,
            start_time=start_time
        )

        with patch('src.utils.toilet_session_utils.get_active_session', AsyncMock(return_value=session)), \
                patch('src.repository.toilet_king.update_king_stats', AsyncMock()), \
                patch('src.repository.toilet_king.get_current_king', AsyncMock(return_value=None)):
            result_session, stars_change, king_info = await end_toilet_session(user, db)

            assert result_session.end_time is not None
            assert result_session.duration is not None
            assert stars_change == -STARS_PENALTY
            assert user.stars >= 0
            db.commit.assert_called_once()
            db.refresh.assert_called_once_with(result_session)


class TestGetUserSessionStats:
    @pytest.mark.asyncio
    async def test_get_stats_with_sessions(self, user, db):
        sessions = [
            ToiletSession(
                user_id=user.id,
                start_time=datetime.utcnow() - timedelta(days=1),
                end_time=datetime.utcnow() - timedelta(days=1) + timedelta(minutes=5),
                duration=300  # 5 min
            ),
            ToiletSession(
                user_id=user.id,
                start_time=datetime.utcnow() - timedelta(days=2),
                end_time=datetime.utcnow() - timedelta(days=2) + timedelta(minutes=15),
                duration=900  # 15 min
            )
        ]

        mock_result = Mock()
        mock_result.scalars().all.return_value = sessions
        db.execute.return_value = mock_result

        stats = await get_user_session_stats(user.id, db)

        assert stats["total_sessions"] == 2
        assert stats["sessions_within_limit"] == 1
        assert stats["success_rate"] == 50.0
        assert stats["total_time"] == 1200
        assert stats["average_time"] == 600.0

    @pytest.mark.asyncio
    async def test_get_stats_no_sessions(self, user, db):
        mock_result = Mock()
        mock_result.scalars().all.return_value = []
        db.execute.return_value = mock_result

        stats = await get_user_session_stats(user.id, db)

        assert stats["total_sessions"] == 0
        assert stats["sessions_within_limit"] == 0
        assert stats["success_rate"] == 0
        assert stats["total_time"] == 0
        assert stats["average_time"] == 0