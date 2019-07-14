"""Module for connecting to database."""

from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import BFF_POSTGRES_OPTIONS


def gen_postgres_link(options: Dict[str, str]) -> str:
    """Generate link for `create_engine` from options dict."""
    link = 'postgresql://'
    link += options['user']
    if options.get('password'):
        link += ':{0}'.format(options['password'])
    link += '@{0}:{1}/'.format(
        options['host'],
        options['port'],
    )
    link += options['database']
    return link


class Database(object):
    """Class for SQLAlchemy connection."""

    def __init__(self) -> None:
        """Create connection for SQLAlchemy."""
        db_link = gen_postgres_link(BFF_POSTGRES_OPTIONS)
        engine = create_engine(db_link)
        session_class = sessionmaker(bind=engine)
        self.session = session_class()

    def close(self) -> None:
        """Close session connection."""
        self.session.close()
