#!/usr/bin/python3

"""Project runner."""

import logging

from aiohttp import web

from src.db import init_db
from src.server import APP
from src.settings import BFF_SERVER_HOST, BFF_SERVER_PORT, DEBUG

if __name__ == '__main__':
    init_db()

    log_level = logging.DEBUG if DEBUG else logging.INFO
    logging.basicConfig(level=log_level)

    web.run_app(
        APP,
        port=BFF_SERVER_PORT,
        host=BFF_SERVER_HOST,
        access_log_format='%t %a "%r" %s',
    )
