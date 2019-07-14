"""Module for games application testing."""


async def test_hello(aiohttp_client, setup_server):
    """Hello world test."""
    client = await aiohttp_client(setup_server)
    resp = await client.get('/games/')
    ok_status = 200
    assert resp.status == ok_status
    text = await resp.text()
    assert 'Games will be here' in text
