from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.i18n.translations import translator

from src.database.db import get_db
from src.services.auth import auth_service
from src.entity.models import User
from src.services.yeti_removal_system import remove_yeti, get_curse_history, apply_yeti_curse, applied_curse

router_curse = APIRouter(prefix="/curse", tags=["Curse"])


@router_curse.post("/remove",
                   description="Знімає прокляття з користувача за зірки, повертає: (успіх, повідомлення, вартість)")
async def remove_yeti_curse(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user),
        t: callable = Depends(translator)
):
    success, message, cost = await remove_yeti(current_user, db, t)
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {
        "success": True,
        "message": message,
        "stars_spent": cost
    }


@router_curse.get("/history", description="Отримує історію зняття проклять користувача")
async def get_curse_removal_history(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user),
        limit: int = 5
):
    try:
        history = await get_curse_history(current_user.id, db, limit)
        return [
            {
                "id": item.id,
                "stars_spent": item.stars_spent,
                "removed_at": item.removed_at
            } for item in history
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_curse.post("/apply",
                   description="target_user_id: ID користувача, на якого накладається прокляття \n\n "
                               "duration: Тривалість прокляття в днях (за замовчуванням 3 дні)")
async def apply_curse(
        target_user_id: int,
        duration: int = 3,  # тривалість в днях
        db: AsyncSession = Depends(get_db),
        t: callable = Depends(translator)
):
    target = await applied_curse(target_user_id, db)
    if not target:
        raise HTTPException(status_code=404, detail=t("curse.errors.user_not_found"))

    # Накладаємо прокляття
    curse_end = await apply_yeti_curse(target, db, duration=timedelta(days=duration))

    return {
        "success": True,
        "message": f"Curse applied until {curse_end}",
        "target_user_id": target_user_id
    }
