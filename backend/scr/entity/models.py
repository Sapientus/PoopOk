from datetime import date

from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class JoinTime:
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[date] = mapped_column(
        'created_at', DateTime, default=func.now(), nullable=True)
    updated_at: Mapped[date] = mapped_column(
        'updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True)


class User(JoinTime, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)

    posts: Mapped["Post"] = relationship("Post", backref="user", cascade="all, delete-orphan")
    comments: Mapped["Comment"] = relationship("Comment", backref="user", cascade="all, delete-orphan")


class Post(JoinTime, Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    comments: Mapped["Comment"] = relationship("Comment", backref="post", cascade="all, delete-orphan")


class Comment(JoinTime, Base):
    __tablename__ = "comments"

    content: Mapped[str] = mapped_column(Text)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
