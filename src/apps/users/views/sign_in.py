""" Module for auth of registered users """

import jwt

from src.core.middleware.request import has_body
from src.db import AIOPG, get_script
from src.core.exceptions import WrongAuthCredentials
from src.apps.users.utils import verify_password
from src.settings import BFF_SECRET_KEY


@has_body
async def view(request):
    """ Auth route handler """

    async with AIOPG['conn'].cursor() as cursor:
        json = await request.json()

        username = json['username']
        password = json['password']

        script = get_script('users', 'auth', {
            'username': username.lower()
        })

        await cursor.execute(script)

        result = await cursor.fetchone()
        if not result:
            raise WrongAuthCredentials()

        if not verify_password(result[2], password):
            raise WrongAuthCredentials()

        # Generate JWT
        payload = {
            'id': result[0]
        }
        token = jwt.encode(payload, BFF_SECRET_KEY, algorithm='HS256')

        return {
            'id': result[0],
            'username': result[1],
            'token': token.decode('UTF-8')
        }
