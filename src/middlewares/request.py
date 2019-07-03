""" All requests wrappers """

from aiohttp import web

from src.exceptions import EmptyRequestBodyError


def has_body(handler):
    """ Check if request have request body """

    async def wrapper(view):
        """ Decorator """
        request = view if isinstance(view, web.Request) else view.request
        if not request.has_body:
            raise EmptyRequestBodyError()

        return await handler(view)

    return wrapper
