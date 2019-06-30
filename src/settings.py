""" BFF settings file. """

import os


BFF_SERVER_PORT: int = int(os.getenv('BFF_SERVER_PORT') or '8000')
BFF_SERVER_HOST: int = os.getenv('BFF_SERVER_HOST') or 'localhost'

BFF_POSTGRES_OPTIONS: dict = {
    'user': os.getenv('BFF_POSTGRES_USER') or 'postgres',
    'host': os.getenv('BFF_POSTGRES_HOST') or 'localhost',
    'port': int(os.getenv('BFF_POSTGRES_PORT') or '5432'),
    'database': os.getenv('BFF_POSTGRES_DBNAME') or 'donkey-engine'
}
if os.getenv('BFF_POSTGRES_PASS'):
    BFF_POSTGRES_OPTIONS['password'] = os.getenv('BFF_POSTGRES_PASS')
