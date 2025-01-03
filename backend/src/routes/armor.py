from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.i18n.translations import translator

from src.database.db import get_db
from src.services.armor_system import get_current_armor_status, update_user_armor, apply_armor_bonus, ArmorType
from src.services.auth import auth_service
from src.entity.models import User

router_armor = APIRouter(prefix="/armor", tags=["Armor"])


@router_armor.get("/status", description="Отримує поточний статус броні користувача")
async def get_armor_status(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user)
):
    try:
        armor_status = await get_current_armor_status(current_user, db)
        return armor_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_armor.post("/update-type", description="Оновлює тип броні користувача та її максимальне значення")
async def update_armor_type(
        armor_type: ArmorType,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user),
        t: callable = Depends(translator)
):
    try:
        await update_user_armor(current_user, armor_type, db)
        return {"message": t("armor.success.type_updated").format(armor_type=armor_type.value)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_armor.post("/apply-bonus", description="Додає тимчасовий бонус до броні")
async def apply_temporary_armor_bonus(
        bonus_amount: int,
        duration_days: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user)
):
    try:
        bonus = await apply_armor_bonus(
            current_user,
            bonus_amount,
            timedelta(days=duration_days),
            db
        )
        return {
            "message": "Armor bonus applied",
            "bonus_id": bonus.id,
            "expires_at": bonus.expires_at
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
