""" Module for registration of new user """

from psycopg2 import errors

from src.core.exceptions import UsernameIsAlreadyExists
from src.core.middleware.request import has_body
from src.db import AIOPG, get_script
from src.apps.users.utils import hash_password


@has_body
async def view(request):
    """ Route handler """

    json = await request.json()

    username = json['username']
    password = json['password']

    async with AIOPG['conn'].cursor() as cursor:
        script = get_script('users', 'registration', {
            'username': username.lower(),
            'password': hash_password(password)
        })

        try:
            await cursor.execute(script)
        except errors.UniqueViolation:  # pylint: disable=maybe-no-member
            raise UsernameIsAlreadyExists()
        else:
            result = await cursor.fetchone()
            return {
                'id': result[0],
                'username': result[1]
            }
