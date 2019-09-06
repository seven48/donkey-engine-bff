"""Module for user model."""

from peewee import CharField

from src.model import BaseModel

username_max_length = 32


class User(BaseModel):
    """User model."""

    username = CharField(
        max_length=username_max_length,
        unique=True,
    )
    password = CharField()
