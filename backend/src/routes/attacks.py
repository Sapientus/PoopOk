from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from src.i18n.translations import translator

from src.database.db import get_db
from src.entity.models import User
from src.repository.status_game import make_attack, get_users_for_attack
from src.schemas.attacks import PoopAttackRequest, PoopAttackResponse, UserForAttackResponse
from src.services import toilet_sessions
from src.services.auth import auth_service

router = APIRouter(prefix='/attacks', tags=['Attacks'])


@router.post("/poop", response_model=PoopAttackResponse,
             description="target_id: ID користувача, якого атакують\n\n stars_spent: кількість витрачених зірок")
async def make_poop_attack(
        attack_data: PoopAttackRequest,
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db),
        t: callable = Depends(translator)
):
    if await toilet_sessions.is_user_frozen(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=t("attack.errors.user_frozen")
        )
    try:
        remaining_stars = current_user.stars - attack_data.stars_spent
        if remaining_stars < 0:
            raise ValueError(t("attack.errors.not_enough_stars"))

        attack, damage, target_armor, t = await make_attack(
            attacker=current_user,
            target_id=attack_data.target_id,
            stars_spent=attack_data.stars_spent,
            db=db,
            t=t
        )

        current_user.stars = remaining_stars
        await db.commit()

        return PoopAttackResponse(
            message=t("attack.success.attack_successful"),
            damage_dealt=damage,
            remaining_stars=remaining_stars,
            target_armor_after_attack=target_armor
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/for-attack", response_model=list[UserForAttackResponse],
            description="Витягуємо список доступних чєліків для атаки")
async def list_users_for_attack(
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db)
):
    users = await get_users_for_attack(current_user.id, db)
    return users
