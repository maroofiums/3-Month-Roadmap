from fastapi import FastAPI, Depends, Request
from models import Todo
from fake_db import todos_db
from auth import login, get_current_user
from rate_limiter import rate_limiter
from cache import get_cached_todos, set_cached_todos

app = FastAPI(title="Final Mini Project")

app.post("/login")(login)

@app.post("/todos")
async def create_todo(
    todo: Todo,
    user=Depends(get_current_user),
    request: Request = None,
    _=Depends(rate_limiter)
):
    todos_db.append(todo.dict())
    set_cached_todos(user, todos_db)
    return {"msg": "Todo added"}

@app.get("/todos")
async def get_todos(
    user=Depends(get_current_user),
    request: Request = None,
    _=Depends(rate_limiter)
):
    cached = get_cached_todos(user)
    if cached:
        return {"source": "cache", "todos": cached}

    set_cached_todos(user, todos_db)
    return {"source": "db", "todos": todos_db}
