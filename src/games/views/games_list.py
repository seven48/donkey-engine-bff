""" Module with games list view """

import json

from aiohttp import web
from src.games.model import Game


class View(web.View):
    """ Games list view """

    async def get(self):
        """ Games list get method """

        games = Game.query().all()
        return {'games': [game.to_dict() for game in games]}

    async def post(self):
        """ Games list post method """

        data = await self.request.post()
        try:
            config = json.loads(data['config'])
        except ValueError:
            raise web.HTTPBadRequest()
        try:
            title = data['title']
        except KeyError:
            raise web.HTTPBadRequest()
        game = Game(title=title, config=config)
        Game.commit(game)
        games = Game.query().all()
        return {'games': [game.to_dict() for game in games]}
