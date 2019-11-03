"""Module for help setup/teardow test database."""

import psycopg2
from peewee_migrations.migrator import Router

from src import settings
from src.db import DATABASE, init_db
from src.games.model import Game

TEST_DB_NAME = 'test-{0}'.format(settings.BFF_POSTGRES_OPTIONS['database'])


def _execute_query(query):
    options = {**settings.BFF_POSTGRES_OPTIONS, 'database': 'postgres'}
    with psycopg2.connect(**options) as connection:
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(query)


def create_db():
    """Test database create."""
    _execute_query('CREATE DATABASE "{0}"'.format(TEST_DB_NAME))
    init_db(TEST_DB_NAME)
    _apply_migrations()
    return DATABASE


async def drop_db():
    """Test database drop."""
    await DATABASE.close_async()
    _execute_query('DROP DATABASE "{0}"'.format(TEST_DB_NAME))


def _apply_migrations():
    """Apply migration to test database."""
    # TODO: load router config from migrations.json
    router = Router(
        database=DATABASE,
        models=[Game],
        migrate_dir='src/migrations',
        migrate_table='migratehistory',
    )
    steps = router.migrate()
    for step in steps:
        step.run()

    # close sync connection after migrations
    DATABASE.close()
