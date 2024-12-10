from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, EmailStr, Field, field_serializer


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=10)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    stars: int | None
    armor: int | None
    is_frozen_until: datetime | None = None
    confirmed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    @field_serializer('created_at', 'updated_at')
    def serialize_datetime(self, dt: datetime | None) -> str | None:
        if dt is None:
            return None
        return dt.strftime("%d.%m.%Y")

    class Config:
        from_attributes = True


class AccessTokenSchema(BaseModel):
    access_token: str
    token_type: Literal['bearer'] = 'bearer'


class RefreshTokenSchema(BaseModel):
    refresh_token: str
    token_type: Literal['bearer'] = 'bearer'


class TokenSchema(AccessTokenSchema, RefreshTokenSchema):
    pass


class RequestEmail(BaseModel):
    email: str | EmailStr
