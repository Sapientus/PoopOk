import pytest
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.entity.models import ToiletSession, User
from src.services.toilet_sessions import (
    is_session_within_limit,
    can_start_new_session,
    is_user_frozen,
    MAX_TOILET_TIME
)


class TestToiletSessionFunctions:
    @pytest.fixture
    def mock_user(self):
        user = User()
        user.id = 1
        user.is_frozen_until = None
        return user

    @pytest.mark.asyncio
    async def test_is_session_within_limit_valid(self):
        session = ToiletSession()
        session.duration = MAX_TOILET_TIME - 1  # трохи менше максимального ліміту

        result = await is_session_within_limit(session)
        assert result is True

    @pytest.mark.asyncio
    async def test_is_session_within_limit_invalid(self):
        session = ToiletSession()
        session.duration = MAX_TOILET_TIME + 1  # більше за максимальний ліміт

        result = await is_session_within_limit(session)
        assert result is False

    @pytest.mark.asyncio
    async def test_is_session_within_limit_no_duration(self):
        session = ToiletSession()
        session.duration = None

        result = await is_session_within_limit(session)
        assert result is False

    @pytest.mark.asyncio
    async def test_can_start_new_session_no_active_sessions(self, mock_user):
        # Налаштування моку бази даних
        mock_db = AsyncMock(spec=AsyncSession)

        # Мок функції get_active_session, щоб повертала None
        mock_db.execute = AsyncMock()
        mock_db.execute.return_value.scalar_one_or_none.return_value = None

        # Виклик функції
        can_start, message = await can_start_new_session(mock_user, mock_db)

        # Перевірки
        assert can_start is True
        assert message == "OK"

    @pytest.mark.asyncio
    async def test_can_start_new_session_active_session_exists(self, mock_user):
        mock_db = AsyncMock(spec=AsyncSession)

        # Мок активної сесії
        active_session = ToiletSession()
        mock_db.execute = AsyncMock()
        mock_db.execute.return_value.scalar_one_or_none.return_value = active_session

        can_start, message = await can_start_new_session(mock_user, mock_db)

        assert can_start is False
        assert "already has an active toilet session" in message

    @pytest.mark.asyncio
    async def test_can_start_new_session_recent_session(self, mock_user):
        mock_db = AsyncMock(spec=AsyncSession)

        # Мок нещодавньої сесії
        recent_session = ToiletSession()
        recent_session.end_time = datetime.utcnow() - timedelta(minutes=30)
        mock_db.execute = AsyncMock()
        mock_db.execute.return_value.scalar_one_or_none.return_value = recent_session

        can_start, message = await can_start_new_session(mock_user, mock_db)

        assert can_start is False
        assert "need to wait at least 1 hour" in message

    @pytest.mark.asyncio
    async def test_is_user_frozen_frozen(self, mock_user):
        # Встановлюємо час заморозки у майбутньому
        mock_user.is_frozen_until = datetime.utcnow() + timedelta(days=1)

        result = await is_user_frozen(mock_user)
        assert result is True

    @pytest.mark.asyncio
    async def test_is_user_frozen_not_frozen(self, mock_user):
        # Встановлюємо час заморозки у минулому
        mock_user.is_frozen_until = datetime.utcnow() - timedelta(days=1)

        result = await is_user_frozen(mock_user)
        assert result is False

    @pytest.mark.asyncio
    async def test_is_user_frozen_no_freeze(self, mock_user):
        # Взагалі без заморозки
        mock_user.is_frozen_until = None

        result = await is_user_frozen(mock_user)
        assert result is False