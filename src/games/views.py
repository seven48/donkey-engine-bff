""" Games view """

from aiohttp import web


class View(web.View):
    """ Games view """

    @staticmethod
    async def get():
        """ Get request handler. """
        return "Games will be here"
