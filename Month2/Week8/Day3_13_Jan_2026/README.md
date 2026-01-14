# Week8 Day3

## 📁 Project Structure

```
redis_fastapi_cache/
│
├── main.py
├── redis_client.py
├── fake_db.py
├── requirements.txt
└── README.md
```

---

## 1️⃣ requirements.txt

```txt
fastapi
uvicorn
redis
```

Install:

```bash
pip install -r requirements.txt
```

---

## 2️⃣ redis_client.py

👉 Handles Redis connection (single responsibility)

```python
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True  # converts bytes → string
)
```

### Why this file?

* Clean architecture
* Redis logic stays separate
* Easy to reuse later (rate limiting, auth, etc.)

---

## 3️⃣ fake_db.py

👉 Simulated database (learning purpose)

```python
def get_todos_from_db():
    print("📦 Fetching data from DB...")
    return [
        {"id": 1, "title": "Learn FastAPI"},
        {"id": 2, "title": "Learn Redis"},
        {"id": 3, "title": "Build Mini Project"}
    ]
```

✅ Best practice:
When learning infra (Redis, auth, caching), **don’t complicate with real DB first**.

---

## 4️⃣ main.py

👉 FastAPI app with Redis caching

```python
from fastapi import FastAPI
import json
from redis_client import redis_client
from fake_db import get_todos_from_db

app = FastAPI(title="FastAPI Redis Cache Demo")

CACHE_KEY = "todos"
CACHE_TTL = 60  # seconds


@app.get("/todos")
def get_todos():
    # 1️⃣ Check Redis cache
    cached_todos = redis_client.get(CACHE_KEY)

    if cached_todos:
        print("⚡ Returning data from Redis cache")
        return json.loads(cached_todos)

    # 2️⃣ Cache miss → fetch from DB
    todos = get_todos_from_db()

    # 3️⃣ Store in Redis with TTL
    redis_client.setex(
        CACHE_KEY,
        CACHE_TTL,
        json.dumps(todos)
    )

    return todos
```

---

## 🧠 Complete Request Flow (Very Important)

```
Client → /todos
   |
   |-- Redis.get("todos")
       |
       |-- HIT → return cached JSON
       |
       |-- MISS → fake DB call
                    |
                    |-- Redis.setex(key, ttl, data)
                    |
                    → return response
```

---

## 5️⃣ README.md

````md
# FastAPI + Redis Caching (Day 3)

## Features
- FastAPI GET endpoint
- Redis caching
- TTL-based cache expiration
- Clean architecture

## How to Run

### 1. Start Redis
```bash
redis-server
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI

```bash
uvicorn main:app --reload
```

### 4. Test

Open:
[http://127.0.0.1:8000/todos](http://127.0.0.1:8000/todos)

## Cache Behavior

* First request → DB fetch
* Next requests → Redis cache (60s)

```

---

## 🧪 How to Verify Cache Works

### First request:
```

📦 Fetching data from DB...

```

### Second request (within 60 sec):
```

⚡ Returning data from Redis cache

```

🔥 That’s real caching.

---

## ⚠️ Common Beginner Mistakes

❌ Forgetting TTL  
❌ Caching POST responses  
❌ Mixing Redis logic inside route file  
❌ Using Redis as DB replacement  

---

## ✅ Best Practices

✔ Clear cache keys (`todos:user_id`)  
✔ TTL always  
✔ Invalidate cache on POST/PUT/DELETE  
✔ Redis = performance layer, not source of truth  

---