import pytest
import json
from httpx import AsyncClient
from fastapi.testclient import TestClient 
from fastapi import status
from main import app 

client = TestClient(app)
base_url = "http://localhost"
res = "" 
data = {
  "title": "title-test",
  "description": "description-test"
}

@pytest.mark.anyio
async def test_create_todo():
  async with AsyncClient(app=app, base_url=base_url) as ac:
    response = await ac.post("/todo/", json=data)
    global res
    res = response.json()
    assert response.status_code == 200

@pytest.mark.anyio
async def test_get_all_todos():
  async with AsyncClient(app=app, base_url=base_url) as ac:
    response = await ac.get("/todo/")
    assert response.status_code == 200

#Complete tests with mongoDB tests