"""Module for games application testing."""

from tests.http_codes import (  # noqa: I001
    HTTP_BAD_REQUEST_CODE, HTTP_NOT_FOUND_CODE, HTTP_OK_CODE,  # noqa: I001
)


async def test_games(aiohttp_client, setup_server):  # noqa: Z217
    """Test for games endpoint."""
    client = await aiohttp_client(setup_server)

    resp = await client.get('/games/')
    assert resp.status == HTTP_OK_CODE
    response_data = await resp.json()
    assert 'games' in response_data['data']
    assert not response_data['data']['games']

    resp = await client.post('/games/', data={'title': '', 'config': 'test'})
    assert resp.status == HTTP_BAD_REQUEST_CODE

    resp = await client.post('/games/', data={'title': 'test', 'config': '""'})
    assert resp.status == HTTP_OK_CODE
    response_data = await resp.json()
    assert 'games' in response_data['data']
    assert response_data['data']['games']
    assert response_data['data']['games'][0]['title'] == 'test'


async def test_game(aiohttp_client, setup_server):  # noqa: Z217
    """Test for game endpoint."""
    client = await aiohttp_client(setup_server)

    resp = await client.get('/games/777')
    assert resp.status == HTTP_NOT_FOUND_CODE

    resp = await client.get('/games/1')
    assert resp.status == HTTP_OK_CODE
    response_data = await resp.json()
    assert response_data['data']
    assert response_data['data']['title'] == 'test'

    resp = await client.put(
        '/games/1', data={'title': '', 'config': 'test'})  # noqa: Z319
    assert resp.status == HTTP_BAD_REQUEST_CODE

    resp = await client.put(
        '/games/1', data={'title': 'test1', 'config': '""'})  # noqa: Z319
    assert resp.status == HTTP_OK_CODE
    response_data = await resp.json()
    assert response_data['data']['title'] == 'test1'

    resp = await client.put(
        '/games/777', data={'title': 'test1', 'config': '""'})  # noqa: Z319
    assert resp.status == HTTP_NOT_FOUND_CODE

    resp = await client.delete('/games/1')
    assert resp.status == HTTP_OK_CODE

    resp = await client.get('/games/1')
    assert resp.status == HTTP_NOT_FOUND_CODE
