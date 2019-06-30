""" Module for working with database """

import aiopg


AIOPG = {
    'conn': None,
    'cur': None
}

async def connect(options):
    """ Make connection to the database with options """

    conn = await aiopg.connect(**options)
    AIOPG['conn'] = conn

    cur = await conn.cursor()
    AIOPG['cur'] = cur

    print('New postgresql connection "{}"'.format(conn.dsn))

async def stop():
    """ Stop database connection """

    AIOPG['conn'].close()
