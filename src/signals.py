""" Module for aiohttp signals """

from src.db import Database


async def on_startup(_):
    """ Function that will called on server starting """

    # Creating the first instance of SQLAlchemy connection
    Database()

async def on_shutdown(_):
    """ Function that will called on server stopping """

    Database().close()
