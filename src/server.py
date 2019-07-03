""" Aiohttp server initialization. """

from aiohttp import web

from src.middlewares import exception
from src.router import ROUTES
from src.signals import on_startup, on_shutdown


APP = web.Application(
    middlewares=[
        exception.catcher
    ]
)

APP.on_startup.append(on_startup)
APP.on_shutdown.append(on_shutdown)

APP.add_routes(ROUTES)
