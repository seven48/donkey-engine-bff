""" Middleware for cathing exceptions. """

from typing import Awaitable, Any, Callable, Coroutine

from aiohttp import web
from aiohttp.web import Application, Request, Response


Handler = Callable[[Request], Awaitable[Any]]
Middleware = Callable[[Request], Coroutine[Any, Any, Response]]

async def catcher(_: Application, handler: Handler) -> Middleware:
    """ Decorator. """
    async def middleware(request: Request) -> Response:
        """ Catching exceptions and coverting it to JSON response. """
        try:
            result = await handler(request)

        except Exception as err:  # pylint: disable=broad-except
            print(str(err))
            response = {
                'status': 'error',
                'data': str(err) or 'Unknown error'
            }

            status = getattr(err, 'status', -1)  # It's default status of aiohttp exceptions

            return web.json_response(
                data=response,
                status=status if status > 0 else 400
            )

        else:
            if isinstance(result, Response):
                return result

            response = {
                'status': 'success',
                'data': result
            }
            status = 200
            return web.json_response(
                data=response,
                status=status
            )

    return middleware
