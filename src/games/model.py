""" Module for games model """

from sqlalchemy import inspect
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.types import JSON

from src.model import Base


class Game(Base):
    """ Game model """

    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String(length=100))
    config = Column(JSON())

    __table_args__ = (UniqueConstraint('id'), UniqueConstraint('title'))

    def to_dict(self, to_serialize=None):
        """ Helper for convert the game instance to dict """
        if not to_serialize:
            to_serialize = inspect(self).attrs
        data = {}
        for attr_name in to_serialize:
            data[attr_name.key] = getattr(self, attr_name.key)
        return data
