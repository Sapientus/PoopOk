import pytest
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import User, YetiCurseRemoval
from src.services.yeti_removal_system import (
    apply_yeti_curse,
    calculate_curse_removal_cost,
    can_remove_curse,
    remove_yeti,
    get_curse_history,
    CurseRemovalCost
)


@pytest.fixture
def mock_user():
    user = User()
    user.id = 1
    user.stars = 100
    user.is_frozen_until = datetime.utcnow() + timedelta(days=5)
    return user


@pytest.mark.asyncio
async def test_apply_yeti_curse(mock_user):
    # Налаштування моку бази даних
    mock_db = AsyncMock(spec=AsyncSession)
    mock_db.commit = AsyncMock()

    # Виклик функції
    frozen_until = await apply_yeti_curse(mock_user, mock_db)

    # Перевірки
    assert frozen_until is not None
    assert isinstance(frozen_until, datetime)
    assert mock_user.is_frozen_until > datetime.utcnow()
    mock_db.commit.assert_called_once()


@pytest.mark.asyncio
async def test_apply_yeti_curse_custom_duration(mock_user):
    mock_db = AsyncMock(spec=AsyncSession)
    mock_db.commit = AsyncMock()

    custom_duration = timedelta(days=7)
    frozen_until = await apply_yeti_curse(mock_user, mock_db, duration=custom_duration)

    assert frozen_until is not None
    assert (frozen_until - datetime.utcnow()).days == 7
    mock_db.commit.assert_called_once()


@pytest.mark.asyncio
async def test_calculate_curse_removal_cost(mock_user):
    # Тест базової вартості зняття прокляття
    cost = await calculate_curse_removal_cost(mock_user)

    expected_cost = (
            CurseRemovalCost.BASE_STARS +
            (5 * CurseRemovalCost.ADDITIONAL_PER_DAY)
    )
    assert cost == expected_cost


@pytest.mark.asyncio
async def test_calculate_curse_removal_cost_not_cursed():
    user = User()
    user.is_frozen_until = None

    cost = await calculate_curse_removal_cost(user)
    assert cost == 0


@pytest.mark.asyncio
async def test_can_remove_curse(mock_user):
    # Користувач має достатньо зірок
    can_remove, message = await can_remove_curse(mock_user)

    assert can_remove is True
    assert message == "OK"


@pytest.mark.asyncio
async def test_can_remove_curse_not_enough_stars(mock_user):
    # Встановлюємо замало зірок для зняття прокляття
    mock_user.stars = 10

    can_remove, message = await can_remove_curse(mock_user)

    assert can_remove is False
    assert "Not enough stars" in message


@pytest.mark.asyncio
async def test_can_remove_curse_not_cursed(mock_user):
    mock_user.is_frozen_until = None

    can_remove, message = await can_remove_curse(mock_user)

    assert can_remove is False
    assert message == "User is not cursed"


@pytest.mark.asyncio
async def test_remove_yeti(mock_user):
    mock_db = AsyncMock(spec=AsyncSession)
    mock_db.add = MagicMock()
    mock_db.commit = AsyncMock()

    initial_stars = mock_user.stars

    success, message, cost = await remove_yeti(mock_user, mock_db)

    assert success is True
    assert message == "Curse removed successfully"
    assert mock_user.is_frozen_until is None
    assert mock_user.stars == initial_stars - cost
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()


@pytest.mark.asyncio
async def test_remove_yeti_not_enough_stars(mock_user):
    mock_user.stars = 10
    mock_db = AsyncMock(spec=AsyncSession)

    success, message, cost = await remove_yeti(mock_user, mock_db)

    assert success is False
    assert "Not enough stars" in message
    assert cost == 0


@pytest.mark.asyncio
async def test_get_curse_history(mock_user):
    mock_db = AsyncMock(spec=AsyncSession)

    # Створення мок-даних історії зняття прокляття
    mock_removals = [
        YetiCurseRemoval(user_id=mock_user.id, stars_spent=20, removed_at=datetime.utcnow()),
        YetiCurseRemoval(user_id=mock_user.id, stars_spent=15, removed_at=datetime.utcnow() - timedelta(days=1))
    ]

    # Налаштування поведінки моку бази даних
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = mock_removals
    mock_db.execute.return_value = mock_result

    # Виклик функції
    history = await get_curse_history(mock_user.id, mock_db)

    # Перевірки
    assert len(history) == 2
    assert all(removal.user_id == mock_user.id for removal in history)

