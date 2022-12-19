import asyncio

from fastapi.testclient import TestClient 
from fastapi import status
from main import app 

client = TestClient(app)

data = {
  "id": "63a08a2d7996ccf443d46ee1",
  "title": "title-test55",
  "description": "description-test55"
}

def test_create_todo():
    loop = asyncio.new_event_loop()
    response = client.post("/todo/", json=data)
    assert response.status_code == status.HTTP_200_OK
    loop.close()

def test_get_all_todos():
    loop = asyncio.new_event_loop()
    response = client.get('/todo/')
    assert response.status_code == status.HTTP_200_OK
    loop.close()    