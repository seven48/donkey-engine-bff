"""Module for pytests fixtures."""

import asyncio

import pytest

from src.server import make
from tests.db_helper import create_db, drop_db


@pytest.fixture(scope='session')
def event_loop(request):
    """
    Redefining event_loop fixture with scope='session'.

    https://github.com/pytest-dev/pytest-asyncio/issues/75#issuecomment-358934457
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def setup_db():
    """Test database setup."""
    create_db()
    yield
    await drop_db()


@pytest.fixture
def setup_server():
    """Server instance initialization."""
    return make()
