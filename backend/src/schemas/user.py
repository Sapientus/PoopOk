from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, EmailStr, Field, field_serializer


class DateTimeSerializerMixin:
    @field_serializer('created_at', 'updated_at')
    def serialize_datetime(self, dt: datetime | None) -> str | None:
        return dt.strftime("%d.%m.%Y") if dt else None

    class Config:
        from_attributes = True


class BaseUserFields(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    confirmed: bool


class UserBasicInfoSchema(BaseUserFields):
    pass


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=10)


class UserResponseAboutMe(BaseUserFields, DateTimeSerializerMixin):
    stars: Optional[int] = None
    armor: Optional[int] = None
    is_frozen_until: Optional[datetime] = None
    avatar: str | None
    created_at: datetime
    updated_at: Optional[datetime] = None


class TokenBaseSchema(BaseModel):
    token_type: Literal['bearer'] = 'bearer'


class AccessTokenSchema(TokenBaseSchema):
    access_token: str


class RefreshTokenSchema(TokenBaseSchema):
    refresh_token: str


class TokenSchema(AccessTokenSchema, RefreshTokenSchema, UserResponseAboutMe):
    pass


class RequestEmail(BaseModel):
    email: EmailStr
