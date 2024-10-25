from fastapi import APIRouter, Depends

from scr.entity.models import User
from scr.schemas.user import UserResponse
from scr.services.auth import auth_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
async def get_current_user(user: User = Depends(auth_service.get_current_user)):
    return user
