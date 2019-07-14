"""Module for aiohttp signals."""

from aiohttp import web

from src.db import Database


async def on_startup(app: web.Application) -> None:
    """Start server operations."""
    # Creating the first instance of SQLAlchemy connection
    app['db'] = Database()


async def on_shutdown(app: web.Application) -> None:
    """Shutdown server operations."""
    app['db'].close()
