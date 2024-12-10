from datetime import datetime
from pydantic import BaseModel


class YetiStatusResponse(BaseModel):
    username: str
    attack_count: int
    is_frozen: bool
    frozen_until: datetime | None

    class Config:
        from_attributes = True
