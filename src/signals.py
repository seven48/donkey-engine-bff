""" Module for aiohttp signals """

from aiohttp import web

from src.db import Database


async def on_startup(_: web.Application) -> None:
    """ Function that will called on server starting """

    # Creating the first instance of SQLAlchemy connection
    Database()

async def on_shutdown(_: web.Application) -> None:
    """ Function that will called on server stopping """

    Database().close()
