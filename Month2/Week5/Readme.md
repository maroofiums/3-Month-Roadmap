

# 🟦 Week 1 (21–27 Dec) – REST API + CRUD (Deep Guide)

## 🎯 Week Goal

By end of this week, tum confidently keh sako:

> “Yes, I can design & build a proper CRUD REST API in FastAPI.”

---

## 📅 Day 1 – REST + FastAPI Basics (21 Dec)

### Concepts (Must Clear)

* **REST** = rules to design APIs
* **Endpoint** = URL + HTTP method
* **FastAPI** = Python framework for APIs

### HTTP Methods (yaad rakhna)

| Method | Meaning     |
| ------ | ----------- |
| GET    | Read data   |
| POST   | Create data |
| PUT    | Update data |
| DELETE | Delete data |

### Minimal FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### Run

```bash
uvicorn main:app --reload
```

### Reality Check

* Browser → **GET only**
* POST/PUT/DELETE → Swagger UI

👉 `http://127.0.0.1:8000/docs`

### Honest Advice

✅ Swagger UI ko apna dost bana lo
❌ FastAPI ko Flask jaisa mat treat karo

---

## 📅 Day 2 – CRUD Concept + Pydantic (22 Dec)

### CRUD ka real meaning

CRUD ≠ endpoints
CRUD = **data lifecycle**

### Data Model (Pydantic)

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

### Fake Database

```python
users_db = []
```

### Create User

```python
@app.post("/users")
def create_user(user: User):
    users_db.append(user)
    return user
```

### Key Logic

```text
Request → Validation → Save → Response
```

### Best Practice

✅ Always use Pydantic
❌ Dict directly mat lo (`request.json()` style)

---

## 📅 Day 3 – Read Operations (23 Dec)

### Get All Users

```python
@app.get("/users")
def get_users():
    return users_db
```

### Get User by ID

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}
```

### Improvement (Next days)

* Status codes
* Exceptions

### Mentor Tip

> Read operations sabse easy hoti hain — yahin confidence build hota hai.

---

## 📅 Day 4 – Update + Delete (24 Dec)

### Update User

```python
@app.put("/users/{user_id}")
def update_user(user_id: int, updated: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated
            return updated
    return {"error": "User not found"}
```

### Delete User

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return {"message": "Deleted"}
    return {"error": "User not found"}
```

### Common Mistake

❌ Logic copy-paste
✅ Reusable thinking develop karo

---

## 📅 Day 5 – Status Codes + HTTPException (25 Dec)

### Proper Error Handling

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

### Status Code Sense

* 200 → OK
* 201 → Created
* 404 → Not Found
* 400 → Bad Request

### Why important?

👉 Recruiter **status codes** dekh kar backend maturity judge karta hai

---

## 📅 Day 6 – Router + Project Structure (26 Dec)

### Structure (Industry-style)

```
app/
 ├─ main.py
 ├─ routers/
 │   └─ users.py
 ├─ schemas.py
```

### Router Example

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def get_users():
    return []
```

### Why?

* Scalable
* Clean
* Readable

---

## 📅 Day 7 – Mini Project + Review (27 Dec)

### 🎯 Mini Project

**User Management API**

* Create user
* Read user(s)
* Update user
* Delete user
* Proper status codes
* Swagger docs clean

### Self-Check

Ask yourself:

* CRUD flow samajh aaya?
* Request → response journey clear?
* Code readable hai?

---

## 🧠 Week 1 Summary (Must Remember)

* REST = rules, not framework
* CRUD = logic lifecycle
* FastAPI = validation + speed
* Swagger = testing tool
* Structure > speed

### Golden Tip 🌟