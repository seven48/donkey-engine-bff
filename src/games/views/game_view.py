"""Module with game view."""

import json
from typing import Dict

from aiohttp import web
from playhouse.shortcuts import model_to_dict

from src.games.model import Game


class View(web.View):
    """Game view."""

    async def get(self) -> Dict:
        """Get method handler."""
        game_id = self.request.match_info['id']

        try:
            game = await Game.manager.get(Game, id=game_id)
        except Game.DoesNotExist:
            raise web.HTTPNotFound()

        return model_to_dict(game)

    async def put(self) -> Dict:
        """Put method handler."""
        game_id = self.request.match_info['id']

        try:
            game = await Game.manager.get(Game, id=game_id)
        except Game.DoesNotExist:
            raise web.HTTPNotFound()

        game_data = await self.request.post()
        try:
            game.config = json.loads(str(game_data['config']))
        except ValueError:
            raise web.HTTPBadRequest()

        title = game_data.get('title')
        if not title:
            raise web.HTTPBadRequest()

        game.title = title

        await Game.manager.update(game)
        return model_to_dict(game)

    async def delete(self) -> str:
        """Delete method handler."""
        game_id = self.request.match_info['id']

        try:
            game = await Game.manager.get(Game, id=game_id)
        except Game.DoesNotExist:
            raise web.HTTPNotFound()

        await Game.manager.delete(game)
        return ''
