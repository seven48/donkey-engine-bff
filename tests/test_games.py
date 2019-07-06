""" Module for games application testing """

async def test_hello(aiohttp_client, setup_server):
    """ Hello world test """

    client = await aiohttp_client(setup_server)
    resp = await client.get("/games/")
    assert resp.status == 200
    text = await resp.text()
    assert "Games will be here" in text
