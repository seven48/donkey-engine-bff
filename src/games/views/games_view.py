"""Module with games list view."""

import json
from typing import Dict

from aiohttp import web

from src.games.model import Game


class View(web.View):
    """Games list view."""

    async def get(self) -> Dict:
        """Games list get method."""
        query = self.request.app['db'].session.query(Game)
        games = query.all()
        return {'games': [game.to_dict() for game in games]}

    async def post(self) -> Dict:  # noqa: Z210
        """Games list post method."""
        game_data = await self.request.post()
        session = self.request.app['db'].session
        query = session.query(Game)
        try:
            config = json.loads(str(game_data['config']))
        except ValueError:
            raise web.HTTPBadRequest()
        try:
            title = game_data['title']
        except KeyError:
            raise web.HTTPBadRequest()
        game = Game(title=title, config=config)
        session.add(game)
        session.commit()
        return {'games': [game.to_dict() for game in query.all()]}
