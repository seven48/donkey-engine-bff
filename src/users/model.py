""" Module for user model """

from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.db import Model


class User(Model):
    """ User model """

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(length=32))
    password = Column(String())

    __table_args__ = (UniqueConstraint('id'), UniqueConstraint('username'))
