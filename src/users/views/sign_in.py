"""Module for authorization handler."""

from typing import Dict, Union

import jwt
from aiohttp.web_request import Request

from src.exceptions import WrongAuthCredentials
from src.middlewares.request import has_body
from src.settings import BFF_SECRET_KEY
from src.users.hash import verify_password
from src.users.model import User


@has_body
async def view(request: Request) -> Dict['str', Union[int, str]]:
    """Handle sign in route."""
    json = await request.json()

    query = request.app['db'].session.query(User)
    user = query.filter(User.username == json['username']).first()

    if not user:
        raise WrongAuthCredentials()

    if not verify_password(user.password, json['password']):
        raise WrongAuthCredentials()

    payload = {
        'id': user.id,
    }

    token = jwt.encode(payload, BFF_SECRET_KEY, algorithm='HS256')

    return {
        'id': user.id,
        'username': user.username,
        'token': token.decode('UTF-8'),
    }
