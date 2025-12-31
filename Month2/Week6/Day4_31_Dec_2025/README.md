
# 🟦 Week 6 – Day 4: Async Database Simulation

## 🎯 Goal
- Samajhna ke **database calls async kyun hoti hain**
- Async DB ka **flow** clear karna
- Fake DB bana kar async behavior simulate karna
- Real async DB (SQLAlchemy async) ke liye mindset ready karna

---

## 🧠 Why Database Calls Are Async?

Database query ka flow:
1. Request DB ko bheji
2. DB data process karta hai
3. Response wapas aata hai

👉 Is beech **server wait karta hai**
👉 Yeh wait = **I/O Bound**

### Solution:
- ❌ Sync → server block
- ✅ Async → server free, dusri requests handle

---

## 🧪 Fake Async Database Call (Simulation)

Real DB ki jagah hum `asyncio.sleep()` use karte hain  
Taake **wait behavior** samajh aaye.

```python
import asyncio

async def fake_db_call():
    await asyncio.sleep(2)  # pretend DB query
    return [
        {"id": 1, "name": "Ali"},
        {"id": 2, "name": "Sara"}
    ]
````

🧠 Meaning:

* 2 seconds DB busy
* FastAPI meanwhile dusra kaam kar sakta hai

---

## 🚀 Async FastAPI Endpoint with Fake DB

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

async def fake_db_call():
    await asyncio.sleep(2)
    return [
        {"id": 1, "name": "Ali"},
        {"id": 2, "name": "Sara"}
    ]

@app.get("/users")
async def get_users():
    users = await fake_db_call()
    return {"users": users}
```

### 🔄 Flow

1. Request `/users` par aayi
2. Async endpoint start hua
3. `await fake_db_call()` → wait
4. Event loop ne dusri requests handle ki
5. Data mila → response return

---

## ⚖️ Sync DB vs Async DB

### ❌ Sync DB (Bad for APIs)

```python
import time

def fake_db_sync():
    time.sleep(2)
    return ["data"]

@app.get("/sync-db")
def sync_db():
    data = fake_db_sync()
    return {"data": data}
```

Problems:

* Server block hota hai
* High traffic mein API slow

---

### ✅ Async DB (Recommended)

```python
@app.get("/async-db")
async def async_db():
    data = await fake_db_call()
    return {"data": data}
```

Benefits:

* Non-blocking
* High concurrency
* FastAPI optimized

---

## 🧪 Multiple Requests Test

### Async:

* 2 requests → parallel wait
* Total time ≈ 2 sec

### Sync:

* 1st request → 2 sec
* 2nd request → 2 sec
* Total ≈ 4 sec

---

## 🔥 Key Mental Model

> **Async DB = “Waiting without blocking”**

* DB slow ho sakta hai
* API fast reh sakti hai
* Server resources waste nahi hotay

---

## ⚠️ Common Mistakes

❌ `time.sleep()` inside async function
❌ Blocking DB drivers with async endpoints
❌ Har function ko async bana dena

---

## ✅ Best Practices

* Async use karo jab **wait involved ho**
* DB, API, File I/O → async
* CPU-heavy work → sync / background / workers

---

## 📝 Practice Task

* `/sync-users` → `time.sleep(2)`
* `/async-users` → `await asyncio.sleep(2)`
* Browser ke multiple tabs se test karo

---

## 🔑 Summary

> Database calls naturally slow hoti hain
> Async use karke **scalability** achieve hoti hai, speed nahi
