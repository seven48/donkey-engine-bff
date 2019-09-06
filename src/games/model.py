"""Module for games model."""

from playhouse.postgres_ext import CharField, JSONField

from src.model import BaseModel


class Game(BaseModel):
    """Game model."""

    title = CharField(
        max_length=100,
        unique=True,
    )
    config = JSONField()
