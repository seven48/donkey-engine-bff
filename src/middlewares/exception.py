"""Middleware for cathing exceptions."""

from typing import Any, Awaitable, Callable, Coroutine

from aiohttp import web
from aiohttp.web import Application, Request, Response

Handler = Callable[[Request], Awaitable[Any]]
Middleware = Callable[[Request], Coroutine[Any, Any, Response]]


async def catcher(_: Application, func: Handler) -> Middleware:
    """Decorator."""
    async def middleware(request: Request) -> Response:
        """Catching exceptions and coverting it to JSON response."""
        try:
            response = await func(request)

        except Exception as err:  # pylint: disable=broad-except
            response = {
                'status': 'error',
                'data': str(err) or 'Unknown error',
            }

            # It's default status of aiohttp exceptions
            status = getattr(err, 'status', -1)
            default_exception = 400

            return web.json_response(
                data=response,
                status=status if status > 0 else default_exception,
            )

        else:
            if isinstance(response, Response):
                return response

            response = {
                'status': 'success',
                'data': response,
            }
            status = 200
            return web.json_response(
                data=response,
                status=status,
            )

    return middleware
