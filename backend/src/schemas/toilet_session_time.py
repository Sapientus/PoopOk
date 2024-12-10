from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ToiletSessionStart(BaseModel):
    pass


class ToiletSessionEnd(BaseModel):
    pass


class ToiletSessionResponse(BaseModel):
    id: int
    user_id: int
    start_time: datetime
    end_time: datetime | None
    duration: int | None

    class Config:
        from_attributes = True


class ActiveToiletSessionResponse(BaseModel):
    id: int
    start_time: datetime
    duration_so_far: int
    is_overtime: bool

    class Config:
        from_attributes = True


class ToiletSessionEndResponse(BaseModel):
    session: ToiletSessionResponse
    stars_change: int
    king_info: Optional[dict] = None
    message: str


class UserSessionStats(BaseModel):
    total_sessions: int   # Загальна кількість сесій
    sessions_within_limit: int  # Кількість сесій в межах ліміту часу
    success_rate: float  # Відсоток успішних сесій (які вклалися в ліміт)
    total_time: int  # Загальний час всіх сесій в секундах
    average_time: float  # Середній час однієї сесії в секундах
