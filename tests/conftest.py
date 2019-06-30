import pytest

from src.server import APP


@pytest.fixture
def setup_server():
    return APP
