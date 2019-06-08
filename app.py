#!/usr/bin/python3

""" Project runner. """

from aiohttp import web

from src.server import APP


if __name__ == "__main__":
    web.run_app(APP)
