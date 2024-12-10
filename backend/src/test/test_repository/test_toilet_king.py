from datetime import datetime
from unittest.mock import Mock

import pytest

from src.entity.models import ToiletKing, User
from src.repository.toilet_session_king import apply_king_bonus, get_current_king, update_king_stats


@pytest.fixture
async def test_user():
    return User(
        id=1,
        username="test_user",
        armor=10,
        max_armor=20
    )


@pytest.fixture
async def test_db():
    mock_db = Mock()

    async def mock_execute(*args, **kwargs):
        return mock_db.execute.return_value

    async def mock_commit():
        return None

    mock_db.execute = Mock()
    mock_db.execute.side_effect = mock_execute
    mock_db.commit.side_effect = mock_commit
    return mock_db


class TestToiletKingFunctions:
    @pytest.mark.asyncio
    async def test_update_king_stats_new_record(self, test_db):
        user_id = 1
        session_duration = 300
        test_db.execute.return_value.scalar_one_or_none.return_value = None

        result = await update_king_stats(user_id, session_duration, test_db)

        assert isinstance(result, ToiletKing)
        assert result.user_id == user_id
        assert result.total_duration == session_duration
        assert result.total_sessions == 1
        assert test_db.add.called

    @pytest.mark.asyncio
    async def test_update_king_stats_existing_record(self, test_db):
        user_id = 1
        session_duration = 300
        existing_king = ToiletKing(
            user_id=user_id,
            date=datetime.utcnow().date(),
            total_duration=500,
            total_sessions=2
        )
        test_db.execute.return_value.scalar_one_or_none.return_value = existing_king

        result = await update_king_stats(user_id, session_duration, test_db)

        assert result.total_duration == 800
        assert result.total_sessions == 3

    @pytest.mark.asyncio
    async def test_get_current_king_exists(self, test_db):
        expected_king = {
            "username": "king_user",
            "total_duration": 1000,
            "total_sessions": 5,
            "date": datetime.utcnow().date()
        }
        mock_king = ToiletKing(
            user_id=1,
            total_duration=expected_king["total_duration"],
            total_sessions=expected_king["total_sessions"],
            date=expected_king["date"]
        )
        test_db.execute.return_value.first.return_value = (mock_king, expected_king["username"])

        result = await get_current_king(test_db)

        assert result == expected_king

    @pytest.mark.asyncio
    async def test_get_current_king_no_king(self, test_db):
        test_db.execute.return_value.first.return_value = None

        result = await get_current_king(test_db)

        assert result is None

    @pytest.mark.asyncio
    async def test_apply_king_bonus_success(self, test_user, test_db):
        king_stats = ToiletKing(
            user_id=test_user.id,
            date=datetime.utcnow().date(),
            armor_bonus_applied=False
        )
        test_db.execute.return_value.scalar_one_or_none.return_value = king_stats

        result = await apply_king_bonus(test_user, test_db)

        assert result is True
        assert test_user.armor == 15
        assert king_stats.armor_bonus_applied is True

    @pytest.mark.asyncio
    async def test_apply_king_bonus_already_applied(self, test_user, test_db):
        king_stats = ToiletKing(
            user_id=test_user.id,
            date=datetime.utcnow().date(),
            armor_bonus_applied=True
        )
        test_db.execute.return_value.scalar_one_or_none.return_value = king_stats

        result = await apply_king_bonus(test_user, test_db)

        assert result is False
        assert test_user.armor == 10

    @pytest.mark.asyncio
    async def test_apply_king_bonus_max_armor(self, test_user, test_db):
        test_user.armor = 18
        king_stats = ToiletKing(
            user_id=test_user.id,
            date=datetime.utcnow().date(),
            armor_bonus_applied=False
        )
        test_db.execute.return_value.scalar_one_or_none.return_value = king_stats

        result = await apply_king_bonus(test_user, test_db)

        assert result is True
        assert test_user.armor == 20
        assert king_stats.armor_bonus_applied is True
