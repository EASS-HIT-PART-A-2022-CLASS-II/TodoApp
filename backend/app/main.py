from fastapi import FastAPI, HTTPException

from model import Todo
from database import (fetch_all_todos, fetch_todo, create_todo, update_todo_data, delete_todo_data)

app = FastAPI(title="Todo List")

@app.get("/")
async def root():
    return {"message": "main window"}

@app.get('/todo/')
async def get_all_todos():
    todos = await fetch_all_todos()
    return todos

@app.get('/todo/{id}')
async def get_todo_by_id(id: str):
    todo = await fetch_todo(id)
    if todo:
        return todo
    raise HTTPException(400, "The record does not exist")

@app.post('/todo/')
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Failed to create new record")

@app.put('/todo/{id}')
async def update_todo(id: str, request: Todo):
    request = {k: v for k, v in request.dict().items() if v is not None}
    updated_todo = await update_todo_data(id, request)
    if updated_todo:
        return ("The record has been updated")
    raise HTTPException(400, "Failed to update the record, the record does not exist")

@app.delete('/todo/{id}')
async def delete_todo(id: str):
    deleted_todo = await delete_todo_data(id)
    if deleted_todo:
        return ("The record has been deleted")
    raise HTTPException(400, "Failed to delete the record, the record does not exist")

