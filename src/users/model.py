""" Module for user model """

from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.model import Base


class User(Base):  # pylint: disable=too-few-public-methods
    """ User model """

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(length=32))
    password = Column(String())

    __table_args__ = (UniqueConstraint('id'), UniqueConstraint('username'))
