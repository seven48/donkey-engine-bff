"""Module for registration handler."""

from aiohttp.web_request import Request

from src.middlewares.request import has_body
from src.users.hash import hash_password
from src.users.model import User


@has_body
async def view(request: Request) -> str:
    """Registration handler."""
    json = await request.json()

    await User.manager.create(
        User,
        username=json['username'],
        password=hash_password(json['password']),
    )

    return 'User registered successfully!'
