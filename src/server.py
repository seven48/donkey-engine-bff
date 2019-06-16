""" Aiohttp server initialization. """

from aiohttp import web

from src.core.middleware import exception
from src.apps.router import ROUTES
from src.signals import on_startup


APP = web.Application(
    middlewares=[
        exception.catcher
    ]
)

APP.on_startup.append(on_startup)

APP.add_routes(ROUTES)
