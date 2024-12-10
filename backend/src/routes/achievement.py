from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.entity.models import User
from src.services.achievement_system import fetch_user_achievements, process_achievements
from src.services.auth import auth_service

router_achievements = APIRouter(prefix="/achievements", tags=["Achievements"])


@router_achievements.get("/", description="Отримує всі досягнення користувача")
async def get_user_achievements(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user)
):
    try:
        achievements = await fetch_user_achievements(current_user, db)
        return achievements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_achievements.post("/check",
                          description="Перевіряє та видає всі доступні досягнення"
                                      "\n\ntoilet_master - За 100 успішних какульок\n\n"
                                      "\n\npoop_warrior - За 50 успішних атак\n\n armor_king - За максимальну броню\n\n"
                                      "\n\nstar_collector - За накопичення 100 зірок\n\n"
                                      "\n\ncurse_breaker - За зняття 5 проклять\n\n")
async def check_and_grant_achievements(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(auth_service.get_current_user)
):
    try:
        results = await process_achievements(current_user, db)

        if not results:
            return {
                "message": "There are no achievements so far",
            }

        return {
            "message": "Achievement check completed",
            "new_achievements": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
