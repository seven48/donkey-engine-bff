"""BFF settings file."""

import os
from types import MappingProxyType
from typing import Mapping

BFF_SECRET_KEY: str = os.getenv('BFF_SECRET_KEY') or 'secret_key'

BFF_SERVER_PORT: int = int(os.getenv('BFF_SERVER_PORT') or '8000')
BFF_SERVER_HOST: str = os.getenv('BFF_SERVER_HOST') or 'localhost'

DEBUG: bool = os.getenv('DEBUG', '').lower() == 'true'

BFF_POSTGRES_OPTIONS: Mapping[str, str] = MappingProxyType({
    'user': os.getenv('BFF_POSTGRES_USER') or 'postgres',
    'host': os.getenv('BFF_POSTGRES_HOST') or 'localhost',
    'port': os.getenv('BFF_POSTGRES_PORT') or '5432',
    'database': os.getenv('BFF_POSTGRES_DBNAME') or 'donkey-engine',
    'password': os.getenv('BFF_POSTGRES_PASS') or '',
})
