""" Module for games application testing """


async def test_games(aiohttp_client, setup_server):
    """ Test for games endpoint """

    client = await aiohttp_client(setup_server)
    resp = await client.get("/games/")
    assert resp.status == 200
    data = await resp.json()
    assert "games" in data["data"]
    assert not data["data"]["games"]

    resp = await client.post("/games/", data={"title": "test", "config": '""'})
    assert resp.status == 200
    data = await resp.json()
    assert "games" in data["data"]
    assert data["data"]["games"]
    assert data["data"]["games"][0]["title"] == "test"


async def test_game(aiohttp_client, setup_server):
    """ Test for game endpoint """

    client = await aiohttp_client(setup_server)
    resp = await client.get("/games/1")
    assert resp.status == 200
    data = await resp.json()
    assert data["data"]
    assert data["data"]["title"] == "test"

    resp = await client.put("/games/1", data={"title": "test1", "config": '""'})
    assert resp.status == 200
    data = await resp.json()
    assert data["data"]["title"] == "test1"

    resp = await client.delete("/games/1")
    assert resp.status == 200
    resp = await client.get("/games/1")
    assert resp.status == 404
