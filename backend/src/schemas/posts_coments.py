from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class CommentBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    content: Optional[str] = None


class CommentResponse(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    title: Optional[str] = None
    content: Optional[str] = None


class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    comments: List[CommentResponse] = []

    model_config = ConfigDict(from_attributes=True)
