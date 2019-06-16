""" BFF settings file. """

import os


BFF_SERVER_PORT: int = os.getenv('BFF_SERVER_PORT') or 8000
BFF_SERVER_HOST: int = os.getenv('BFF_SERVER_HOST') or 'localhost'

BFF_POSTGRES_URL: str = (
    os.getenv('BFF_POSTGRES_URL') or 'postgresql://postgres@localhost:5432/donkey-engine'
)
