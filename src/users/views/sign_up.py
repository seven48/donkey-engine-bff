""" Module for registration handler """

from src.middlewares.request import has_body
from src.users.utils import hash_password
from src.users.model import User


@has_body
async def view(request):
    """ Registration handler """

    json = await request.json()

    user = User(
        username=json['username'],
        password=hash_password(json['password'])
    )

    user.commit()

    return "User registered successfully!"
