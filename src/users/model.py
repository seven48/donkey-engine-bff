"""Module for user model."""

from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.model import Base


class User(Base):
    """User model."""

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)  # noqa: A003
    username = Column(String(length=32))  # noqa: Z432
    password = Column(String())

    __table_args__ = (UniqueConstraint('id'), UniqueConstraint('username'))
