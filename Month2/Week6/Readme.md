# 🟦 WEEK 6 – Async / Await (28 Dec – 3 Jan)

## 🎯 Week Goal

* Async ka **real use-case** samajhna
* FastAPI mein **kab async, kab sync** use karna
* Mini async project bana ke confidence 💪

---

## 📅 Day 1 – Sync vs Async (28 Dec)

### 🔹 Sync kya hota hai?

```text
Task A → wait → Task B → wait → Task C
```

Example:

* DB call (2 sec)
* API call (3 sec)
* Total = **5 sec**

Code mindset:

```python
def get_data():
    time.sleep(2)
```

---

### 🔹 Async kya hota hai?

```text
Task A → wait (side pe)  
Task B chal raha  
Task C chal raha  
```

Real life example:

* **Sync** = bank ki line mein kharay rehna
* **Async** = token le ke side pe kaam karna

👉 Async = *waiting time waste nahi hota*

⚠️ Important:

> Async = fast CPU nahi
> Async = **smart waiting**

---

## 📅 Day 2 – async / await basics (29 Dec)

### 🔹 Basic async function

```python
import asyncio

async def get_data():
    await asyncio.sleep(2)
    return "Data ready"
```

### Rules (EXAM LEVEL IMPORTANT)

1. `await` ❌ outside `async`
2. `async` function call karne ke liye:

```python
await get_data()
```

### Big confusion clear:

❌ Async ≠ multithreading
✅ Async = I/O wait handle karna

Use async when:

* DB call
* API call
* File read/write
* Network request

---

## 📅 Day 3 – Async FastAPI Endpoints (30 Dec)

### 🔹 Async endpoint

```python
@app.get("/items")
async def read_items():
    return {"items": []}
```

### FastAPI async kyun pasand karta hai?

* Thousands of requests
* Waiting time overlap ho jata hai
* High performance APIs

Backend thinking:

> **Agar endpoint I/O bound hai → async**

---

## 📅 Day 4 – Async DB Simulation (31 Dec)

Abhi real DB nahi, fake delay se samjho.

```python
import asyncio

@app.get("/users")
async def get_users():
    await asyncio.sleep(1)  # fake DB delay
    return {"users": []}
```

### Yahan kya ho raha?

* Server wait kar raha hai
* Lekin block nahi ho raha
* Dusre users serve ho rahe hain

Golden line:

> DB calls = I/O bound
> Async yahin shine karta hai ✨

---

## 📅 Day 5 – Background Tasks (1 Jan)

Kab kaam **response ke baad** karna ho:

Examples:

* Email send
* Logs write
* Notifications

### FastAPI BackgroundTasks

```python
from fastapi import BackgroundTasks

def log_action(msg: str):
    print(msg)

@app.post("/login")
async def login(background_tasks: BackgroundTasks):
    background_tasks.add_task(log_action, "User logged in")
    return {"message": "Login successful"}
```

User ko response **turant** milta hai
Background kaam side pe hota rehta hai

---

## 📅 Day 6 – Mini Async API Project (2 Jan)

### 📌 Project: Async Todo API

Features:

* Async CRUD endpoints
* Fake async DB delay
* Background logging

Example:

```python
@router.post("/todos")
async def create_todo(todo: Todo, background_tasks: BackgroundTasks):
    await asyncio.sleep(1)
    todos.append(todo)
    background_tasks.add_task(log_action, f"Todo added: {todo.id}")
    return todo
```

Yahan tum use kar rahe ho:

* `async def`
* `await`
* `BackgroundTasks`

👉 Ye **real backend pattern** hai

---

## 📅 Day 7 – Review & Decision Making (3 Jan)

Apne aap se yeh sawal poochho:

### ❓ Kahan async use karna chahiye?

✅ DB calls
✅ External APIs
✅ File operations

### ❓ Kahan sync better hai?

✅ Simple calculations
✅ CPU heavy logic
✅ No waiting involved

Backend maturity:

> **Har jagah async likhna galat hai**

---

## 🔑 Week 6 One-Line Rule (Golden)

> **Async sirf tab use karo jab “wait” ho —
> warna sync zyada simple aur safe hota hai.**

---

## 🧠 Week 6 Summary

* Async = smart waiting
* await = pause without blocking
* FastAPI async = performance boost
* BackgroundTasks = post-response work
* Decision > syntax