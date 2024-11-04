from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from backend.scr.entity.posts_comments import Post, Comment
from backend.scr.schemas.posts_coments import PostCreate, CommentCreate, PostUpdate, CommentUpdate


async def get_posts(db: AsyncSession):
    result = await db.execute(select(Post).options(selectinload(Post.comments)))
    return result.scalars().all()


async def get_post(db: AsyncSession, post_id: int):
    result = await db.execute(select(Post).where(Post.id == post_id).options(selectinload(Post.comments)))
    return result.scalar_one_or_none()


async def create_post(db: AsyncSession, post: PostCreate):
    db_post = insert(Post).values(
        title=post.title,
        content=post.content
    )
    result = await db.execute(db_post)
    await db.commit()
    result_resp = {**post.model_dump(), "id": result.lastrowid}
    return result_resp


async def update_post_crud(db: AsyncSession, post_id: int, post_update: PostUpdate):
    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()
    if post:
        if post_update.title is not None:
            post.title = post_update.title
        if post_update.content is not None:
            post.content = post_update.content
        await db.commit()
        await db.refresh(post)
        return post
    return None


async def delete_post(db: AsyncSession, post_id: int):
    result = await db.execute(select(Post).where(Post.id == post_id).options(selectinload(Post.comments)))
    post = result.scalar_one_or_none()
    if post:
        await db.delete(post)
        await db.commit()
        return post
    return None


async def create_comment(db: AsyncSession, post_id: int, comment: CommentCreate):
    db_comment = insert(Comment).values(
        content=comment.content,
        post_id=post_id
    )
    result = await db.execute(db_comment)
    await db.commit()
    result_resp = {**comment.model_dump(), "id": result.lastrowid}
    return result_resp


async def update_comment_crud(db: AsyncSession, comment_id: int, comment_update: CommentUpdate):
    result = await db.execute(select(Comment).where(Comment.id == comment_id))
    comment = result.scalar_one_or_none()
    if comment:
        if comment_update.content is not None:
            comment.content = comment_update.content
        await db.commit()
        await db.refresh(comment)
        return comment
    return None


async def delete_comment(db: AsyncSession, comment_id: int):
    result = await db.execute(select(Comment).where(Comment.id == comment_id))
    comment = result.scalar_one_or_none()
    if comment:
        await db.delete(comment)
        await db.commit()
        return comment
    return None
