import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, AsyncMock
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import User
from src.repository.status_game import get_users_for_attack, make_attack, calculate_attack_damage


@pytest.fixture
async def db():
    """Mock для AsyncSession"""
    mock_db = AsyncMock(spec=AsyncSession)
    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()
    mock_db.execute = AsyncMock()
    mock_db.add = AsyncMock()
    return mock_db


@pytest.fixture
def attacker():
    return User(
        id=1,
        username="attacker",
        stars=100,
        armor=0,
        attack_count=0
    )


@pytest.fixture
def target():
    return User(
        id=2,
        username="target",
        stars=100,
        armor=50,
        attack_count=0
    )


class TestCalculateAttackDamage:
    @pytest.mark.asyncio
    async def test_calculate_damage_with_armor(self, target):
        stars_spent = 70
        damage, new_armor = await calculate_attack_damage(target, stars_spent)
        assert damage == 20
        assert new_armor == 0

    @pytest.mark.asyncio
    async def test_calculate_damage_without_armor(self, target):
        target.armor = 0
        stars_spent = 70
        damage, new_armor = await calculate_attack_damage(target, stars_spent)
        assert damage == 70
        assert new_armor == 0

    @pytest.mark.asyncio
    async def test_calculate_damage_partial_armor(self, target):
        stars_spent = 30
        damage, new_armor = await calculate_attack_damage(target, stars_spent)
        assert damage == 0
        assert new_armor == 20


class TestMakeAttack:
    @pytest.mark.asyncio
    async def test_make_attack_success(self, attacker, target, db):
        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = target
        db.execute.return_value = mock_result

        with patch('src.services.status_yeti.check_yeti_status', return_value=(False, None)), \
                patch('src.services.status_yeti.update_user_yeti_status'):
            attack, damage, new_armor = await make_attack(attacker, target.id, 70, db)

            assert attack.attacker_id == attacker.id
            assert attack.target_id == target.id
            assert attack.stars_spent == 70
            assert attack.damage_dealt == 20
            assert new_armor == 0
            assert target.attack_count == 1
            assert db.add.call_count == 2
            await db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_make_attack_with_yeti_freeze(self, attacker, target, db):
        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = target
        db.execute.return_value = mock_result

        freeze_until = datetime.utcnow() + timedelta(hours=1)

        with patch('src.services.status_yeti.check_yeti_status', return_value=(True, freeze_until)), \
                patch('src.services.status_yeti.update_user_yeti_status') as mock_update_yeti:
            attack, damage, new_armor = await make_attack(attacker, target.id, 70, db)

            assert mock_update_yeti.called
            assert mock_update_yeti.call_args[0] == (target, freeze_until, db)

    @pytest.mark.asyncio
    async def test_make_attack_target_not_found(self, attacker, db):
        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = None
        db.execute.return_value = mock_result

        with pytest.raises(ValueError) as exc_info:
            await make_attack(attacker, 999, 70, db)
        assert str(exc_info.value) == "Target user not found"


class TestGetUsersForAttack:
    @pytest.mark.asyncio
    async def test_get_users_success(self, attacker, target, db):
        mock_result = Mock()
        mock_result.scalars().all.return_value = [target]
        db.execute.return_value = mock_result

        users = await get_users_for_attack(attacker.id, db)

        assert len(users) == 1
        assert users[0] == target
        assert db.execute.called

    @pytest.mark.asyncio
    async def test_get_users_empty_list(self, attacker, db):
        mock_result = Mock()
        mock_result.scalars().all.return_value = []
        db.execute.return_value = mock_result

        users = await get_users_for_attack(attacker.id, db)

        assert len(users) == 0
