"""Module for pytests fixtures."""

import pytest

from src.server import make
from tests.db_helper import create_db, drop_db


@pytest.fixture(scope='session', autouse=True)
def setup_db():
    """Test database setup."""
    create_db()
    yield
    drop_db()


@pytest.fixture
def setup_server():
    """Server instance initialization."""
    return make()
