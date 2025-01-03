from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.entity.models import Post, Comment, User
from src.schemas.posts_coments import PostCreate, CommentCreate, PostUpdate, CommentUpdate


async def get_all_posts(db: AsyncSession):
    stmt = select(Post).options(selectinload(Post.comments)).order_by(Post.created_at.desc())
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_post_by_id(db: AsyncSession, post_id: int):
    stmt = select(Post).where(Post.id == post_id).options(selectinload(Post.comments))
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_post(db: AsyncSession, post_data: PostCreate, current_user: User):
    new_post = Post(**post_data.model_dump(), user_id=current_user.id)
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post, ['comments'])
    return new_post


async def update_post(db: AsyncSession, post_id: int, post_data: PostUpdate, current_user: User):
    stmt = select(Post).where(Post.id == post_id)
    result = await db.execute(stmt)
    post = result.scalar_one_or_none()

    if not post:
        return None

    if post.user_id != current_user.id:
        return None
    for key, value in post_data.model_dump(exclude_unset=True).items():
        setattr(post, key, value)
    await db.commit()
    await db.refresh(post)

    return post


async def delete_post(db: AsyncSession, post_id: int, current_user: User):
    stmt = select(Post).where(Post.id == post_id)
    result = await db.execute(stmt)
    post = result.scalar_one_or_none()

    if not post or post.user_id != current_user.id:
        return False

    await db.delete(post)
    await db.commit()
    return True


async def create_comment(db: AsyncSession, post_id: int, comment_data: CommentCreate, current_user: User, t: callable):
    post_stmt = select(Post).where(Post.id == post_id)
    post_result = await db.execute(post_stmt)
    post = post_result.scalar_one_or_none()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=t("posts.errors.comments_error")
        )
    new_comment = Comment(
        post_id=post_id,
        user_id=current_user.id,
        **comment_data.model_dump()
    )
    db.add(new_comment)
    await db.commit()
    await db.refresh(new_comment)
    return new_comment


async def update_comment(db: AsyncSession,
                         comment_id: int,
                         comment_data: CommentUpdate,
                         current_user: User,
                         t: callable):
    stmt = select(Comment).where(Comment.id == comment_id)
    result = await db.execute(stmt)
    comment = result.scalar_one_or_none()

    if not comment:
        return None

    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=t("auth.errors.authentication_required")
        )
    for key, value in comment_data.model_dump(exclude_unset=True).items():
        setattr(comment, key, value)

    await db.commit()
    await db.refresh(comment)

    return comment


async def delete_comment(db: AsyncSession,
                         comment_id: int,
                         current_user: User,
                         t: callable):
    stmt = select(Comment).where(Comment.id == comment_id)
    result = await db.execute(stmt)
    comment = result.scalar_one_or_none()

    if not comment:
        return None

    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=t("auth.errors.authentication_required")
        )

    await db.delete(comment)
    await db.commit()

    return comment
