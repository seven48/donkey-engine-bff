"""Module for aiohttp signals."""

import aioreloader
from aiohttp.web import Application


async def on_startup(app: Application) -> None:
    """Start server operations."""
    aioreloader.start()


async def on_shutdown(app: Application) -> None:
    """Shutdown server operations."""
