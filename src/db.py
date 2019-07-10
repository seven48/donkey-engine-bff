""" Module for connecting to database """

from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import (
    BFF_POSTGRES_OPTIONS
)


class Database:
    """ Class for SQLAlchemy connection """

    INSTANCE = None

    def __init__(self) -> None:
        """ Creating connection for SQLAlchemy """

        db_link = self.gen_postgres_link(BFF_POSTGRES_OPTIONS)
        engine = create_engine(db_link)
        session_class = sessionmaker(bind=engine)
        self.session = session_class()

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
