""" Module for registration handler """

from src.core.middleware.request import has_body
from src.apps.users.utils import hash_password
from src.apps.users.model import User


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
