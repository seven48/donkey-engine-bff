""" Module for registration handler """

from aiohttp.web_request import Request

from src.middlewares.request import has_body
from src.users.utils import hash_password
from src.users.model import User


@has_body
async def view(request: Request) -> str:
    """ Registration handler """

    json = await request.json()

    user = User(
        username=json['username'],
        password=hash_password(json['password'])
    )

    request.app['db'].session.add(user)
    request.app['db'].session.commit()

    return "User registered successfully!"
