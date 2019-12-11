"""Routes list."""

from aiohttp import web

from src.games.views.game_view import View as GameView
from src.games.views.games_view import View as GamesListView
from src.users.views.sign_in import view as sign_in_view
from src.users.views.sign_up import view as sign_up_view

routes = [
    web.view('/games/', GamesListView),
    web.view(r'/games/{id:\d+}', GameView),
    web.route('POST', '/sign_up', sign_up_view),
    web.route('POST', '/sign_in', sign_in_view),
]
