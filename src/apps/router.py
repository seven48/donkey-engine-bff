""" Routes list. """

from aiohttp import web

from src.apps.games.views import View as GamesView


ROUTES = [
    web.view('/games/', GamesView)
]
