"""All requests wrappers."""

from typing import Any, Callable

from aiohttp.web import Request, View

from src.exceptions import EmptyRequestBodyError


def has_body(func: Callable) -> Callable:
    """Check if request have request body."""
    async def wrapper(view: View) -> Any:
        """Decorator."""
        request = view if isinstance(view, Request) else view.request
        if not request.has_body:
            raise EmptyRequestBodyError()

        return await func(view)

    return wrapper
