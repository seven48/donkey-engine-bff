""" Module for working with database """

import aiopg


AIOPG = {
    'conn': None
}

def get_script(app, scenario, params):
    """ Return scenario by name with specified parameters """

    path = 'src/apps/{}/sql/{}.sql'.format(app, scenario)
    with open(path, 'r') as file:
        script = file.read().format(**params)
        return script

async def connect(options):
    """ Make connection to the database with options """

    conn = await aiopg.connect(**options)
    AIOPG['conn'] = conn

    print('New postgresql connection "{}"'.format(conn.dsn))

async def stop():
    """ Stop database connection """

    AIOPG['conn'].close()
