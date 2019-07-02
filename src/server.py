""" Aiohttp server initialization. """

from aiohttp import web

from src.core.middleware import exception
from src.apps.router import ROUTES


APP = web.Application(
    middlewares=[
        exception.catcher
    ]
)

APP.add_routes(ROUTES)
