from typing import List

from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.i18n.translations import translator

from src.database.db import get_db
from src.entity.models import User
from src.repository import posts_comments
from src.routes.users import get_current_user
from src.schemas.posts_coments import (
    PostCreate,
    CommentCreate,
    PostUpdate,
    CommentUpdate, PostResponse, CommentResponse
)

router = APIRouter(prefix='/comments_and_posts', tags=['Comments and Posts'])


@router.get("/", response_model=List[PostResponse])
async def get_all_posts(db: AsyncSession = Depends(get_db)):
    posts = await posts_comments.get_all_posts(db)
    return posts


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db), t: callable = Depends(translator)):
    post = await posts_comments.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=t("posts.errors.not_found"))
    return post


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_new_post(post: PostCreate, db: AsyncSession = Depends(get_db),
                          current_user: User = Depends(get_current_user)):
    return await posts_comments.create_post(db, post, current_user)


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(post_id: int,
                      post_update: PostUpdate,
                      db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user),
                      t: callable = Depends(translator)):
    updated_post = await posts_comments.update_post(db, post_id, post_update, current_user)
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=t("posts.errors.not_found"))
    return updated_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int,
                      db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user),
                      t: callable = Depends(translator)):
    result = await posts_comments.delete_post(db, post_id, current_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=t("posts.errors.not_found"))


@router.post("/{post_id}/comments", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(post_id: int,
                         comment: CommentCreate,
                         db: AsyncSession = Depends(get_db),
                         current_user: User = Depends(get_current_user),
                         t: callable = Depends(translator)
                         ):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=t("auth.errors.authentication_required")
        )
    return await posts_comments.create_comment(db, post_id, comment, current_user, t)


@router.put("/comments/{comment_id}", response_model=CommentResponse)
async def update_comment(comment_id: int,
                         comment_update: CommentUpdate,
                         db: AsyncSession = Depends(get_db),
                         current_user: User = Depends(get_current_user),
                         t: callable = Depends(translator)):
    updated_comment = await posts_comments.update_comment(db, comment_id, comment_update, current_user, t)
    if not updated_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=t("posts.errors.comments_error"))
    return updated_comment


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(comment_id: int,
                         db: AsyncSession = Depends(get_db),
                         current_user: User = Depends(get_current_user),
                         t: callable = Depends(translator)):
    result = await posts_comments.delete_comment(db, comment_id, current_user, t)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=t("posts.errors.comments_error"))
