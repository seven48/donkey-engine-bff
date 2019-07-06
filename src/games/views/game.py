""" Module with game view """

import json

from aiohttp import web

from src.games.model import Game


class View(web.View):
    """ Game view """

    async def get(self):
        """ Get method handler. """

        game_id = self.request.match_info['id']
        game = Game.query().get(game_id)
        if not game:
            raise web.HTTPNotFound()

        return game.to_dict()  # json.dumps(game.to_dict())

    async def put(self):
        """ Put method handler. """

        game_id = self.request.match_info['id']
        game = Game.query().get(game_id)
        if not game:
            raise web.HTTPNotFound()

        data = await self.request.post()
        try:
            game.config = json.loads(data['config'])
        except ValueError:
            raise web.HTTPBadRequest()
        try:
            game.title = data['title']
        except KeyError:
            raise web.HTTPBadRequest()

        Game.commit(game)
        return game.to_dict()

    async def delete(self):
        """ Delete method handler. """

        game_id = self.request.match_info['id']
        game = Game.query().get(game_id)
        if not game:
            raise web.HTTPNotFound()
        Game.delete(game)
        return ""
