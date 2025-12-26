

# 🟦 Day 6 – Routers + Clean Project Structure

## 🎯 Day 6 Goal

By end of today:

* Samajh jao **kyun router use hota hai**
* FastAPI project ko **professional structure** do
* Code readability + scalability improve ho

---

## 1️⃣ Problem with single `main.py`

Ab tak hum sab kuch yahin likh rahe thay:

```python
main.py
- models
- routes
- logic
```

❌ Issues:

* File bohot bari ho jati hai
* Team work mushkil
* Future features add karna pain

Backend rule:

> **Jitna code barhta hai, structure utna zaroori hota hai**

---

## 2️⃣ Industry-style Folder Structure

Aaj se yeh follow karo:

```
app/
 ├─ main.py
 ├─ routers/
 │   └─ users.py
 ├─ schemas.py
```

### Reason:

* `main.py` → app entry
* `routers/` → endpoints
* `schemas.py` → data models

---

## 3️⃣ Move User Model → `schemas.py`

### `app/schemas.py`

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

✅ Single source of truth
❌ Models har file mein copy nahi

---

## 4️⃣ Create Router → `users.py`

### `app/routers/users.py`

```python
from fastapi import APIRouter, HTTPException
from app.schemas import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users_db = []

@router.post("/", status_code=201)
def create_user(user: User):
    for u in users_db:
        if u.id == user.id:
            raise HTTPException(
                status_code=400,
                detail="User already exists"
            )
    users_db.append(user)
    return user


@router.get("/")
def get_users():
    return users_db


@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}")
def update_user(user_id: int, updated: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
```

---

## 5️⃣ Update `main.py`

### `app/main.py`

```python
from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="User Management API")

app.include_router(users.router)
```

Run:

```bash
uvicorn app.main:app --reload
```

Swagger:
👉 `/docs`

---

## 6️⃣ Why Routers are Powerful

* Logical separation
* Easy to add:

  * `/products`
  * `/orders`
* Teams work parallel

Think future:

> Har feature = new router

---

## 7️⃣ Common Beginner Mistakes (Avoid)

❌ Logic + models mixed
❌ Single giant file
❌ Not using tags / prefixes

✅ Clean separation
✅ Readable folders
✅ Scalability mindset

---

## 🧠 Day 6 Summary

* Routers = modular APIs
* `schemas.py` = data contracts
* `main.py` = entry point
* Structure = backend maturity
