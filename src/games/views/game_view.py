"""Module with game view."""

import json
from typing import Dict

from aiohttp import web
from sqlalchemy.orm import sessionmaker as SessionClass  # noqa: N812

from src.games.model import Game


class View(web.View):
    """Game view."""

    def get_session(self) -> SessionClass:
        """Return current db session."""
        return self.request.app['db'].session

    async def get(self) -> Dict:
        """Get method handler."""
        game_id = self.request.match_info['id']
        query = self.get_session().query(Game)
        game = query.get(game_id)
        if not game:
            raise web.HTTPNotFound()

        return game.to_dict()

    async def put(self) -> Dict:
        """Put method handler."""
        game_id = self.request.match_info['id']
        query = self.get_session().query(Game)
        game = query.get(game_id)
        if not game:
            raise web.HTTPNotFound()

        game_data = await self.request.post()
        try:
            game.config = json.loads(str(game_data['config']))
        except ValueError:
            raise web.HTTPBadRequest()
        try:
            game.title = game_data['title']
        except KeyError:
            raise web.HTTPBadRequest()

        self.get_session().commit()
        return game.to_dict()

    async def delete(self) -> str:
        """Delete method handler."""
        game_id = self.request.match_info['id']
        query = self.request.app['db'].session.query(Game)
        game = query.get(game_id)
        if not game:
            raise web.HTTPNotFound()
        self.get_session().delete(game)
        self.get_session().commit()
        return ''
