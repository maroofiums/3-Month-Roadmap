**Week 6 – Day 6: Mini Async API Project**
---

## 🎯 Day 6 Goal

* Async CRUD endpoints banayein
* Fake async DB simulate karein
* Background logging implement karein
* Real-world FastAPI async API ka feel lein

---

## 1️⃣ Project Overview

### Mini Project: **Async Todo API**

Features:

1. Async CRUD operations
2. Fake DB delay (`await asyncio.sleep()`)
3. BackgroundTasks logging (item create/update/delete)

Directory Structure (simple):

```
week6_day6/
│
├─ main.py
├─ models.py
└─ fake_db.py
```

---

## 2️⃣ Fake DB (Simulation)

```python
# fake_db.py
import asyncio

todos = []

async def get_todos():
    await asyncio.sleep(1)  # simulate DB delay
    return todos

async def add_todo(todo: dict):
    await asyncio.sleep(1)
    todos.append(todo)
    return todo
```

---

## 3️⃣ Models (Pydantic)

```python
# models.py
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False
```

---

## 4️⃣ FastAPI App (Async + Background)

```python
# main.py
from fastapi import FastAPI, BackgroundTasks
from models import Todo
from fake_db import get_todos, add_todo

app = FastAPI()

# Background logging function
def log_action(msg: str):
    print(msg)  # For simplicity; could write to file

# Get all todos
@app.get("/todos")
async def read_todos():
    todos_list = await get_todos()
    return {"todos": todos_list}

# Create a new todo
@app.post("/todos")
async def create_todo(todo: Todo, background_tasks: BackgroundTasks):
    new_todo = await add_todo(todo.dict())
    background_tasks.add_task(log_action, f"Todo added: {todo.id}")
    return new_todo
```

---

## 5️⃣ Step-by-Step Flow

1. **Client hits `/todos` GET**

   * `read_todos()` async
   * `await get_todos()` → wait 1 sec
   * Event loop free → other requests served
   * Response: all todos

2. **Client hits `/todos` POST**

   * `create_todo()` async
   * `await add_todo()` → wait 1 sec
   * BackgroundTasks → log_action() fired **after response**
   * Response sent immediately

---

## 6️⃣ Why This Structure Rocks

* **Async endpoints** → server free during wait
* **Fake async DB** → real DB feel
* **BackgroundTasks** → logging/email after response
* **CRUD ready** → easily extendable

---

## 7️⃣ Optional Extensions (Extra Learning)

* Update todo → `/todos/{id}` PUT (async + log)
* Delete todo → `/todos/{id}` DELETE (async + log)
* Add **query params** → filter completed todos
* Connect to **real async DB** later (`SQLAlchemy async`, `asyncpg`)

---

## 8️⃣ Practice Task 

1. Run API:

```bash
uvicorn main:app --reload
```

2. Test GET `/todos` → empty list
3. Test POST `/todos` → new todo added
4. Observe console → background log printed
5. Open multiple tabs → notice async + background effect

---
