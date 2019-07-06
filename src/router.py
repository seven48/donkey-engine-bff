""" Routes list. """

from aiohttp import web

from src.games.views.games_list import View as GamesListView
from src.games.views.game import View as GameView
from src.users.views.sign_up import view as sign_up_view
from src.users.views.sign_in import view as sign_in_view


ROUTES = [
    web.view('/games/', GamesListView),
    web.view(r'/games/{id:\d+}', GameView),
    web.route('POST', '/sign_up', sign_up_view),
    web.route('POST', '/sign_in', sign_in_view)
]
