from fastapi import FastAPI
from redis_client import redis_client
from fake_db import fake_data
import json

app = FastAPI()

CACHE_KEY = "todos"
CACHE_TTL = 60  

@app.get("/todos")
async def get_todos():
    cached_todos = redis_client.get(CACHE_KEY)
    if cached_todos:
        todos = json.loads(cached_todos)
        return {"source": "cache", "todos": todos}

    todos = fake_data
    redis_client.setex(CACHE_KEY, CACHE_TTL, json.dumps(todos))
    return {"source": "database", "todos": todos}
