"""Games view."""

from aiohttp import web


class View(web.View):
    """Games view."""

    @staticmethod  # noqa: Z433, Z453  # it's temp view
    async def get() -> str:
        """Get request handler."""
        return 'Games will be here'
