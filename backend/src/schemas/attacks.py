from datetime import datetime

from pydantic import BaseModel, Field


class PoopAttackRequest(BaseModel):
    target_id: int
    stars_spent: int = Field(ge=1, le=5)


class PoopAttackResponse(BaseModel):
    message: str
    damage_dealt: int
    remaining_stars: int
    target_armor_after_attack: int
    attack_timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True


class UserForAttackResponse(BaseModel):
    id: int
    username: str
    stars: int
    is_frozen_until: datetime | None
    armor: int

    class Config:
        from_attributes = True
