"""Module with games list view."""

from json.decoder import JSONDecodeError
from typing import Dict

from aiohttp import web
from playhouse.shortcuts import model_to_dict

from src.games.model import Game


class View(web.View):
    """Games list view."""

    async def get(self) -> Dict:
        """Games list get method."""
        games = await Game.manager.execute(Game.select())
        return {'games': [model_to_dict(game) for game in games]}

    async def post(self) -> Dict:
        """Games list post method."""
        if not await self._is_request_valid():
            raise web.HTTPBadRequest()

        game_data = await self.request.json()
        game = await Game.manager.create(
            Game,
            title=game_data['title'],
            config=game_data['config'],
        )
        return {'games': [model_to_dict(game)]}

    async def _is_request_valid(self) -> bool:
        try:
            game_data = await self.request.json()
        except JSONDecodeError:
            return False

        if not game_data.get('title'):
            return False

        return True
