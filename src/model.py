"""Module for BaseModel initialization."""

from peewee import Model
from peewee_async import Manager

from src.db import DATABASE


class BaseModel(Model):
    """Base model class which specifies orm manager and Postgresql database."""

    manager = Manager(DATABASE)

    class Meta(object):
        """Model metadata."""

        database = DATABASE
