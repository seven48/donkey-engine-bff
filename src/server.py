"""Aiohttp server initialization."""

from aiohttp.web import Application

from src.middlewares import exception
from src.router import routes
from src.signals import on_shutdown, on_startup


def make() -> Application:
    """Server instance initialization."""
    app = Application(
        middlewares=[
            exception.catcher,
        ],
    )

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app.add_routes(routes)

    return app


APP = make()
