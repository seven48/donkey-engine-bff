""" Module for working with database """

from gino import Gino


DB = Gino()


async def connect(url):
    """ Make connection to the database with url """
    return await DB.set_bind(url)
