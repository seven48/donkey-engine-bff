"""Alembic auto generated settings."""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from src.db import gen_postgres_link
from src.games.model import Game  # noqa: F401
from src.model import Base
from src.settings import BFF_POSTGRES_OPTIONS
from src.users.model import User  # noqa: F401

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def get_database_url():
    """Generate database url."""
    return gen_postgres_link(
        BFF_POSTGRES_OPTIONS,
    )


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = get_database_url()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    configuration = {
        'sqlalchemy.url': get_database_url(),
    }

    connectable = engine_from_config(
        configuration,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
