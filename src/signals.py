"""Module for aiohttp signals."""

from aiohttp.web import Application


async def on_startup(app: Application) -> None:
    """Start server operations."""


async def on_shutdown(app: Application) -> None:
    """Shutdown server operations."""
