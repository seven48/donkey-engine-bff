""" Module for pytests fixtures """

import pytest

from src.server import APP


@pytest.fixture
def setup_server():
    """ Server instance initialization """

    return APP
