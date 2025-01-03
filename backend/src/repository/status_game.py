from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import PoopAttack, User
from src.services.status_yeti import check_yeti_status, update_user_yeti_status


async def calculate_attack_damage(target: User, stars_spent: int) -> tuple[int, int]:
    """ Розраховує шкоду та залишок броні цілі після атаки з урахуванням макс. броні """
    damage = max(stars_spent - target.armor, 0)
    new_armor = max(target.armor - stars_spent, 0)
    return damage, new_armor


async def make_attack(attacker: User, target_id: int, stars_spent: int, db: AsyncSession, t: callable):
    query = select(User).where(User.id == target_id)
    result = await db.execute(query)
    target = result.scalar_one_or_none()

    if not target:
        raise ValueError(t("user.not_found"))
    should_freeze, freeze_until = await check_yeti_status(target_id, db)  # test
    if should_freeze:  # test
        await update_user_yeti_status(target, freeze_until, db)  # test

    damage, new_armor = await calculate_attack_damage(target, stars_spent)

    target.armor = new_armor
    target.attack_count += 1  # test

    attack = PoopAttack(
        attacker_id=attacker.id,
        target_id=target_id,
        stars_spent=stars_spent,
        damage_dealt=damage
    )

    db.add(attack)
    db.add(target)
    await db.commit()

    return attack, damage, new_armor


async def get_users_for_attack(current_user_id: int, db: AsyncSession):
    query = select(User).where(User.id != current_user_id)
    result = await db.execute(query)
    users = result.scalars().all()
    return users
