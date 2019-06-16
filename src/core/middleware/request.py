""" All requests wrappers """

from src.core.exceptions import EmptyRequestBodyError


def has_body(handler):
    """ Check if request have request body """

    async def wrapper(view):
        """ Decorator """
        if not view.request.has_body:
            raise EmptyRequestBodyError()

        return await handler(view)

    return wrapper
