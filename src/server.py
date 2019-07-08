""" Aiohttp server initialization. """

from aiohttp.web import Application

from src.middlewares import exception
from src.router import ROUTES
from src.signals import on_startup, on_shutdown


def make() -> Application:
    """ Server instance initialization """

    app = Application(
        middlewares=[
            exception.catcher
        ]
    )

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app.add_routes(ROUTES)

    return app


APP = make()
