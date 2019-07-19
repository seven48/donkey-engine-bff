"""Module for games model."""

from typing import Any, Dict

from sqlalchemy import Column, Integer, String, UniqueConstraint, inspect
from sqlalchemy.types import JSON

from src.model import Base


class Game(Base):
    """Game model."""

    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)  # noqa: A003
    title = Column(String(length=100))
    config = Column(JSON())

    __table_args__ = (UniqueConstraint('id'), UniqueConstraint('title'))

    def to_dict(self, to_serialize: Any = None) -> Dict:
        """Do convert the game instance to dict."""
        if not to_serialize:
            to_serialize = inspect(self).attrs
        game_data = {}
        for attr_name in to_serialize:
            game_data[attr_name.key] = getattr(self, attr_name.key)
        return game_data
