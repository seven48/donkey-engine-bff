""" Module for users application testing """

import json

SUCCESS_USERNAME = 'username'
SUCCESS_PASSWORD = 'pass'

async def test_registration(aiohttp_client, setup_server):
    """ Test for /sing_up endpoint """

    client = await aiohttp_client(setup_server)
    url = '/sign_up'

    # Test registration with ordinary conditions
    resp = await client.post(
        url,
        data=json.dumps({
            'username': SUCCESS_USERNAME,
            'password': SUCCESS_PASSWORD
        })
    )
    data = await resp.json()

    assert resp.status == 200
    assert data['status'] == 'success'
    assert data['data'] == 'User registered successfully!'

async def test_authorization(aiohttp_client, setup_server):
    """ Testcase for /sign_in engpoint """

    client = await aiohttp_client(setup_server)
    url = '/sign_in'

    # Test auth with ordinary conditions
    resp = await client.post(
        url,
        data=json.dumps({
            'username': SUCCESS_USERNAME,
            'password': SUCCESS_PASSWORD
        })
    )
    data = await resp.json()

    assert resp.status == 200
    assert data['status'] == 'success'
    assert data['data']['username'] == SUCCESS_USERNAME
    assert isinstance(data['data']['id'], int)
    assert isinstance(data['data']['token'], str)
