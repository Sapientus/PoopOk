from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=10)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    created_at: Optional[datetime]

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
