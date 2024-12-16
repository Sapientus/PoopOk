from datetime import datetime

from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, func, Boolean, Index
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class JoinTime:
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column('created_at', DateTime(timezone=True), default=func.now(),
                                                 nullable=True)
    updated_at: Mapped[datetime] = mapped_column('updated_at', DateTime(timezone=True), default=func.now(),
                                                 onupdate=func.now(), nullable=True)


class User(JoinTime, Base):
    __tablename__ = "users"

    __table_args__ = (
        Index("idx_email", "email"),
        Index("idx_username", "username"),
    )

    username: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    stars: Mapped[int] = mapped_column(default=10)
    armor: Mapped[int] = mapped_column(default=10)
    armor_type: Mapped[str] = mapped_column(String(20), default="basic")
    max_armor: Mapped[int] = mapped_column(default=20)
    is_frozen_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True,
                                                             default=None)
    attack_count: Mapped[int] = mapped_column(default=0)
    posts = relationship("Post", back_populates="user", lazy='joined')
    comments = relationship("Comment", back_populates="user", lazy='joined')


class PoopAttack(JoinTime, Base):
    __tablename__ = "poop_attacks"

    attacker_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    target_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    stars_spent: Mapped[int] = mapped_column(nullable=False)
    damage_dealt: Mapped[int] = mapped_column(Integer, nullable=False)

    target = relationship("User", foreign_keys=[target_id], lazy="selectin")
    attacker = relationship("User", foreign_keys=[attacker_id], lazy="selectin")


class ToiletSession(JoinTime, Base):
    __tablename__ = "toilet_sessions"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=func.now())
    end_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    duration: Mapped[int | None] = mapped_column(Integer, nullable=True)

    user = relationship("User", backref="toilet_sessions")


class ToiletKing(JoinTime, Base):
    __tablename__ = "toilet_kings"

    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.current_date(), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_duration: Mapped[int] = mapped_column(Integer, default=0)
    total_sessions: Mapped[int] = mapped_column(Integer, default=0)
    armor_bonus_applied: Mapped[bool] = mapped_column(default=False)

    user = relationship("User", backref="king_records")

    __table_args__ = (
        Index("idx_toilet_king_date", date),
    )


class YetiCurseRemoval(JoinTime, Base):
    __tablename__ = "yeti_curse_removals"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    stars_spent: Mapped[int] = mapped_column(nullable=False)
    removed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=False)
    user = relationship("User", backref="curse_removals")


class ArmorBonus(JoinTime, Base):
    __tablename__ = "armor_bonuses"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    bonus_amount: Mapped[int] = mapped_column(nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    user = relationship("User", backref="armor_bonuses")


class UserAchievement(JoinTime, Base):
    __tablename__ = "user_achievements"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    achievement_type: Mapped[str] = mapped_column(String(50), nullable=False)
    earned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=False)

    user = relationship("User", backref="achievements")


class Post(JoinTime, Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan", lazy="selectin")
    user = relationship("User", back_populates="posts")


class Comment(JoinTime, Base):
    __tablename__ = "comments"

    content: Mapped[str] = mapped_column(Text)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    post = relationship(Post, back_populates="comments")
    user = relationship("User", back_populates="comments")
