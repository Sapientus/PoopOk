from typing import List

from fastapi import FastAPI, Depends, HTTPException, APIRouter, Response
from sqlalchemy.ext.asyncio import AsyncSession

from scr.database.db import get_db
from scr.schemas.posts_coments import (
    Post,
    PostCreate,
    CommentCreate,
    PostUpdate,
    CommentUpdate
)
from scr.repository.posts_comments import (
    get_posts,
    get_post,
    create_post,
    create_comment,
    delete_post,
    delete_comment,
    update_post_crud,
    update_comment_crud
)

router = APIRouter(prefix='/auth', tags=['Comments and Posts'])


@router.post("/posts", response_model=Post)
async def create_new_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    return await create_post(db=db, post=post)


@router.get("/posts", response_model=List[Post])
async def read_posts(db: AsyncSession = Depends(get_db)):
    return await get_posts(db=db)


@router.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int, db: AsyncSession = Depends(get_db)):
    db_post = await get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post_update: PostUpdate, db: AsyncSession = Depends(get_db)):
    db_update_post = await update_post_crud(db=db, post_id=post_id, post_update=post_update)
    if db_update_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_update_post


@router.delete("/posts/{post_id}", status_code=204)
async def remove_post(post_id: int, db: AsyncSession = Depends(get_db)):
    db_post = await delete_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return Response(status_code=204)


@router.post("/posts/{post_id}/comments", response_model=CommentCreate)
async def create_new_comment(post_id: int, comment: CommentCreate, db: AsyncSession = Depends(get_db)):
    return await create_comment(db=db, post_id=post_id, comment=comment)


@router.delete("/comments/{comment_id}", status_code=204)
async def remove_comment(comment_id: int, db: AsyncSession = Depends(get_db)):
    db_comment = await delete_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return Response(status_code=204)


@router.put("/comments/{comment_id}", response_model=CommentUpdate)
async def update_comment(comment_id: int, comment_update: CommentUpdate, db: AsyncSession = Depends(get_db)):
    db_update_comment = await update_comment_crud(db=db, comment_id=comment_id, comment_update=comment_update)
    if db_update_comment is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_update_comment
