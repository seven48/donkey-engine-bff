""" Module for pytests fixtures """

import pytest

from src.server import make


@pytest.fixture
def setup_server():
    """ Server instance initialization """

    return make()
