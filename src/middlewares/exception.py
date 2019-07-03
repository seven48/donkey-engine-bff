""" Middleware for cathing exceptions. """

from aiohttp import web


async def catcher(_, handler):
    """ Decorator. """
    async def middleware(request):
        """ Catching exceptions and coverting it to JSON response. """
        try:
            result = await handler(request)

        except Exception as err:  # pylint: disable=broad-except
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
            if isinstance(result, web.Response):
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
