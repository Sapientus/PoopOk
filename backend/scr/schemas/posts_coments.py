from pydantic import BaseModel
from typing import List, Optional


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    content: Optional[str] = None


class Comment(CommentBase):
    id: int
    post_id: int
    user_id: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    title: Optional[str] = None
    content: Optional[str] = None


class Post(PostBase):
    id: int
    user_id: int
    comments: List[Comment] = []

    class Config:
        from_attributes = True
