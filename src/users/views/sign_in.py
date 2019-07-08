""" Module for authorization handler """

from typing import Dict, Union

from aiohttp.web_request import Request
import jwt

from src.middlewares.request import has_body
from src.users.model import User
from src.exceptions import WrongAuthCredentials
from src.users.utils import verify_password
from src.settings import BFF_SECRET_KEY


@has_body
async def view(request: Request) -> Dict['str', Union[int, str]]:
    """ Authorization handler """

    json = await request.json()

    query = User.query().filter(User.username == json['username']).first()

    if not query:
        raise WrongAuthCredentials()

    if not verify_password(query.password, json['password']):
        raise WrongAuthCredentials()

    payload = {
        'id': query.id
    }

    token = jwt.encode(payload, BFF_SECRET_KEY, algorithm='HS256')

    return {
        'id': query.id,
        'username': query.username,
        'token': token.decode('UTF-8')
    }
