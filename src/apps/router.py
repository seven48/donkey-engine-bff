""" Routes list. """

from aiohttp import web

from src.apps.games.views import View as GamesView
from src.apps.users.views.sign_up import view as sign_up_view


ROUTES = [
    web.view('/games/', GamesView),
    web.route('POST', '/account/sign_up', sign_up_view)
]
