
# 🟦 Day 7 – Mini Project + Review

## 🎯 Day 7 Goal

By end of today:

* CRUD + Error Handling + Routers + Pydantic ka **integration**
* Full working API ready for GitHub
* Swagger documentation ready
* Backend confidence strong 💪

---

# Project Idea: **Todo App API**

Simple, but covers everything:

* Users can **create todos**
* **Read, update, delete** todos
* Error handling
* Proper folder structure

---

## 1️⃣ Folder Structure (Industry Style)

```
todo_app/
 ├─ app/
 │   ├─ main.py
 │   ├─ routers/
 │   │   └─ todos.py
 │   ├─ schemas.py
 ├─ README.md
```

---

## 2️⃣ `schemas.py` – Data Models

```python
from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
```

---

## 3️⃣ `routers/todos.py` – CRUD Endpoints

```python
from fastapi import APIRouter, HTTPException
from app.schemas import Todo

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

todos_db = []

@router.post("/", status_code=201)
def create_todo(todo: Todo):
    for t in todos_db:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todos_db.append(todo)
    return todo

@router.get("/")
def get_todos():
    return todos_db

@router.get("/{todo_id}")
def get_todo(todo_id: int):
    for t in todos_db:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/{todo_id}")
def update_todo(todo_id: int, updated: Todo):
    for i, t in enumerate(todos_db):
        if t.id == todo_id:
            todos_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    for t in todos_db:
        if t.id == todo_id:
            todos_db.remove(t)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
```

---

## 4️⃣ `main.py` – App Entry

```python
from fastapi import FastAPI
from app.routers import todos

app = FastAPI(title="Todo API")

app.include_router(todos.router)
```

Run:

```bash
uvicorn app.main:app --reload
```

Swagger:
👉 `http://127.0.0.1:8000/docs`

---

## 5️⃣ Mini Quiz (Self Check)

1. What HTTP method to **create** a todo?
2. Which **status code** for successful creation?
3. What happens if you try to GET a non-existing todo?
4. Where do you define data validation rules?
5. Why use routers instead of single main.py?

Answer these to yourself — confirm **Week 1 concepts solid**.

---

## 6️⃣ Bonus Tips for Day 7

* Always test all endpoints in Swagger
* Try **invalid data** → check errors
* Make sure **CRUD + Error handling** works together
* Add `README.md` with instructions

---

## ✅ Day 7 Outcome

* Fully working **Todo API** with CRUD + validation + error handling
* Proper **routers + schemas + structure**
* Swagger documentation ready
* **Week 1 backend foundation solidified**

---

