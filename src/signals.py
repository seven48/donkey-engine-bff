""" All aiohttp signals and events """

from src.settings import BFF_POSTGRES_URL
from src.db import connect


async def on_startup(_):
    """ Function that will called on server starting """
    await connect(BFF_POSTGRES_URL)
