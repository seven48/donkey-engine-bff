""" Module for aiohttp signals """

from aiohttp import web

from src.db import Database


async def on_startup(app: web.Application) -> None:
    """ Function that will called on server starting """

    # Creating the first instance of SQLAlchemy connection
    app['db'] = Database()

async def on_shutdown(app: web.Application) -> None:
    """ Function that will called on server stopping """

    app['db'].close()
