""" Module for connecting to database """

from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from src.settings import (
    BFF_POSTGRES_OPTIONS
)


Base: DeclarativeMeta = declarative_base()


class Database:
    """ Class singleton for SQLAlchemy connection """

    INSTANCE = None

    def __init__(self) -> None:
        """ Creating connection for SQLAlchemy """

        db_link = self.gen_postgres_link(BFF_POSTGRES_OPTIONS)
        engine = create_engine(db_link)
        session_class = sessionmaker(bind=engine)
        self.session = session_class()
        self.base = declarative_base()

    def __new__(cls, *args: tuple, **kwargs: dict) -> 'Database':
        """ Implementation of singleton """

        if not cls.INSTANCE:
            cls.INSTANCE = super(cls, Database).__new__(cls)
            cls.INSTANCE.__init__(*args, **kwargs)

        return cls.INSTANCE

    def close(self) -> None:
        """ Close session connection """

        self.session.close()

    @staticmethod
    def gen_postgres_link(options: Dict[str, str]) -> str:
        """ Generate link for `create_engine` from options dict """

        link = 'postgresql://'
        link += options['user']
        if options.get('password'):
            link += ':{}'.format(options['password'])
        link += '@{}:{}/'.format(
            options['host'],
            options['port']
        )
        link += options['database']
        return link


class Model(Base):
    """ Abstract base model """

    __abstract__ = True

    def commit(self) -> None:
        """ Save changes to session commit """

        database = Database()
        database.session.add(self)
        database.session.commit()

    @classmethod
    def query(cls) -> Query:
        """ Get session query """

        database = Database()
        return database.session.query(cls)
