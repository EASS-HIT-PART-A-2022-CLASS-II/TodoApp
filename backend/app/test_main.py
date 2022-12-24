import pytest
import json
from httpx import AsyncClient
from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)
base_url = "http://localhost"
todo_id = ""
data = json.loads('{"title": "title-test", "description": "description-test"}')
expected_data = json.loads(
    '{"id": "" , "title": "title-test", "description": "description-test"}'
)
updated_data = json.loads(
    '{"title": "title-test-updated", "description": "title-test-updated"}'
)


@pytest.mark.anyio
async def test_create_todo():
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post("/todo/", json=data)
        response_id = await ac.get("/todo/id/title-test")
        global todo_id
        todo_id = str(response_id.text).replace('"', "")
        assert response.status_code == 200
        expected_data["id"] = todo_id
        assert response.json() == expected_data


@pytest.mark.anyio
async def test_get_all_todos():
    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.get("/todo/")
        assert response.status_code == 200
        expected_data["id"] = todo_id
        assert response.json() == [expected_data]


@pytest.mark.anyio
async def test_get_todo_by_id():
    async with AsyncClient(app=app, base_url=base_url) as ac:
        url = "/todo/{id}".format(id=todo_id)
        response = await ac.get(url)
        assert response.status_code == 200
        expected_data["id"] = todo_id
        assert response.json() == expected_data


@pytest.mark.anyio
async def test_update_todo():
    async with AsyncClient(app=app, base_url=base_url) as ac:
        url = "/todo/{id}".format(id=todo_id)
        response = await ac.put(url, json=updated_data)
        assert response.status_code == 200
        assert response.text == '"The record has been updated"'


@pytest.mark.anyio
async def test_delete_todo():
    async with AsyncClient(app=app, base_url=base_url) as ac:
        url = "/todo/{id}".format(id=todo_id)
        response = await ac.delete(url)
        assert response.status_code == 200
        assert response.text == '"The record has been deleted"'
