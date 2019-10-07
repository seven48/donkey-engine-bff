"""Module for users application testing."""

import json

from tests.http_codes import HTTP_BAD_REQUEST_CODE, HTTP_OK_CODE

SUCCESS_USERNAME = 'username'
WRONGS_USERNAME = 'wrong'
SUCCESS_PASSWORD = 'pass'  # noqa: S105


async def test_signup_success(aiohttp_client, setup_server):
    """Test success result of registration."""
    client = await aiohttp_client(setup_server)
    url = '/sign_up'

    resp = await client.post(
        url,
        data=json.dumps({
            'username': SUCCESS_USERNAME,
            'password': SUCCESS_PASSWORD,
        }),
    )
    json_response = await resp.json()

    assert resp.status == HTTP_OK_CODE
    assert json_response['status'] == 'success'
    assert json_response['data'] == 'User registered successfully!'


async def test_signup_existing_user(aiohttp_client, setup_server):
    """Test registration with existing user."""
    client = await aiohttp_client(setup_server)
    url = '/sign_up'

    resp = await client.post(
        url,
        data=json.dumps({
            'username': SUCCESS_USERNAME,
            'password': SUCCESS_PASSWORD,
        }),
    )
    json_response = await resp.json()

    assert resp.status == HTTP_BAD_REQUEST_CODE
    assert json_response['status'] == 'error'


async def test_signin_success(aiohttp_client, setup_server):
    """Test auth with ordinary conditions."""
    client = await aiohttp_client(setup_server)
    url = '/sign_in'

    resp = await client.post(
        url,
        data=json.dumps({
            'username': SUCCESS_USERNAME,
            'password': SUCCESS_PASSWORD,
        }),
    )
    json_response = await resp.json()

    assert resp.status == HTTP_OK_CODE
    assert json_response['status'] == 'success'
    json_data = json_response['data']
    assert json_data['username'] == SUCCESS_USERNAME
    assert isinstance(json_data['id'], int)
    assert isinstance(json_data['token'], str)


async def test_signin_bad_credentials(aiohttp_client, setup_server):
    """Test auth with bad credentials."""
    client = await aiohttp_client(setup_server)
    url = '/sign_in'

    resp = await client.post(
        url,
        data=json.dumps({
            'username': WRONGS_USERNAME,
            'password': SUCCESS_PASSWORD,
        }),
    )
    json_response = await resp.json()

    assert resp.status == HTTP_BAD_REQUEST_CODE
    assert json_response['status'] == 'error'
    assert json_response['data'] == 'Wrong username or password'
