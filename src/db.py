"""Module for declare database."""

from peewee_async import PostgresqlDatabase

from src import settings

DATABASE = PostgresqlDatabase(None)

default_name = settings.BFF_POSTGRES_OPTIONS['database']


def init_db(db_name: str = default_name) -> None:
    """
    Init database.

    May init real/test database depends on argument `db_name`.
    """
    init_args = ('port', 'host', 'user', 'password')
    init_params = {}
    for option in settings.BFF_POSTGRES_OPTIONS:
        if option in init_args:
            init_params[option] = settings.BFF_POSTGRES_OPTIONS[option]

    DATABASE.init(db_name, **init_params)
