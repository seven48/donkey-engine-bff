""" Aiohttp server initialization. """

from aiohttp import web

from src.middlewares import exception
from src.router import ROUTES
from src.signals import on_startup, on_shutdown


def make():
    """ Server instance initialization """

    app = web.Application(
        middlewares=[
            exception.catcher
        ]
    )

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app.add_routes(ROUTES)

    return app


APP = make()
