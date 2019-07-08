""" Routes list. """

from aiohttp import web

from src.games.views import View as GamesView
from src.users.views.sign_up import view as sign_up_view
from src.users.views.sign_in import view as sign_in_view


ROUTES = [
    web.view('/games/', GamesView), # type: ignore | aiohttp fix it in 4 version
    web.route('POST', '/sign_up', sign_up_view),
    web.route('POST', '/sign_in', sign_in_view)
]
