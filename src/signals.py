""" All aiohttp signals and events """

from src.settings import (BFF_POSTGRES_OPTIONS)
from src.db import connect, stop


async def on_startup(_):
    """ Function that will called on server starting """

    await connect(BFF_POSTGRES_OPTIONS)

async def on_shutdown(_):
    """ Function that will called on server stop """

    await stop()
