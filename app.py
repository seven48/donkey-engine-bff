#!/usr/bin/python3

"""Project runner."""

from aiohttp import web

from src.server import APP
from src.settings import BFF_SERVER_HOST, BFF_SERVER_PORT

if __name__ == '__main__':
    web.run_app(
        APP,
        port=BFF_SERVER_PORT,
        host=BFF_SERVER_HOST,
    )
