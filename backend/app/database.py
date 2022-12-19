from model import Todo
from bson.objectid import ObjectId

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://todo-app-DB', 27017)

database = client['todo']

collection= database.todo

def todo_json(todo)-> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"]
    }
    
    
async def fetch_all_todos():
    todos = []
    async for todo in collection.find():
        todos.append(todo_json(todo))
    return todos
    
async def fetch_todo(id):
    todo = await collection.find_one({"_id": ObjectId(id)})
    if todo:
        return todo_json(todo)

async def create_todo(todo_data: dict) -> dict:
    todo = await collection.insert_one(todo_data)
    new_todo = await collection.find_one({"_id": todo.inserted_id})
    return todo_json(new_todo)        

async def update_todo_data(id: str, data: dict):
    todo = await collection.find_one({"_id": ObjectId(id)})
    if todo:
        updated_todo = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_todo:
            return True
        return False

async def delete_todo_data(id: str):
    todo = await collection.find_one({"_id": ObjectId(id)})
    if todo:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    return False

