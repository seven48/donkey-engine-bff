"""Routes list."""

from aiohttp import web

from src.games.views import View as GamesView
from src.users.views.sign_in import view as sign_in_view
from src.users.views.sign_up import view as sign_up_view

routes = [
    web.view('/games/', GamesView),  # type: ignore
    web.route('POST', '/sign_up', sign_up_view),
    web.route('POST', '/sign_in', sign_in_view),
]
