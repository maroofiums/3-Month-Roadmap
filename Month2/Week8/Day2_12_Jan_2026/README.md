
# 🟦 Week 8 – Day 2: Redis Basics

## 🎯 Day 2 Goal

* Understand **key → value store**
* Learn **TTL** (Time To Live)
* Know **how to connect Redis with Python**
* Prepare for **FastAPI caching tomorrow**

---

## 1️⃣ What Redis Really Is

* Redis = **Remote Dictionary** (or key-value store) in memory
* Extremely fast (microseconds response)
* Data stored as **key → value**

### 🔹 Key → Value Analogy

```
key: "user:admin:todos"
value: [{"id":1,"title":"Learn FastAPI"}]
```

* Key is like a **label**
* Value is the **actual data**
* Can expire automatically (TTL)

---

## 2️⃣ TTL (Time To Live)

* Every key can have a **timer**
* After TTL expires → Redis deletes key
* Helps:

  * Avoid stale data
  * Free memory

Example:

```
SET key "todos" value "[{...}]" EX 60
```

* Key = todos
* Value = your list
* EX 60 = expires in 60 seconds

---

## 3️⃣ Installing Redis

1️⃣ Install Redis locally

* **Windows** → Use [Redis for Windows](https://github.com/tporadowski/redis/releases)
* **Linux/Mac** → `brew install redis` / `sudo apt install redis-server`

2️⃣ Start Redis server:

```bash
redis-server
```

3️⃣ Test Redis CLI:

```bash
redis-cli ping
```

Response should be:

```
PONG
```

✅ Redis is running

---

## 4️⃣ Python Client for Redis

Install **redis-py** library:

```bash
pip install redis
```

Basic connection example:

```python
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# Set a key with TTL
r.set("todos:admin", "[{'id':1,'title':'Learn FastAPI'}]", ex=60)

# Get a key
data = r.get("todos:admin")
print(data.decode())  # Redis returns bytes
```

---

## 5️⃣ Key Points for Production

* Use **structured keys** → `resource:user_id`

  * Example: `todos:admin`, `user:123:profile`
* Always set **TTL** for temporary data
* **Don’t store huge objects** (Redis memory is precious)
* Use **JSON for complex data**

  * `json.dumps()` before saving
  * `json.loads()` after fetching

---

## 6️⃣ Practical Example (Simple)

```python
import redis, json

r = redis.Redis(host="localhost", port=6379, db=0)

# Cache user todos
todos = [{"id":1,"title":"Learn FastAPI"}]
r.set("todos:admin", json.dumps(todos), ex=60)

# Later...
cached_todos = r.get("todos:admin")
if cached_todos:
    todos = json.loads(cached_todos)
    print("From cache:", todos)
else:
    print("Cache miss → fetch from DB")
```

---

## 7️⃣ What Redis Will Do in Week 8 Project

* **Cache GET /todos** responses
* TTL = 30–60 seconds (or whatever fits)
* On **POST /todos**, invalidate cache → ensure latest data
* Rate limiting: Redis stores **request counts per user/IP**


---

## ✅ Day 2 Summary

* Redis = **fast in-memory key-value store**
* TTL = controls **cache expiration**
* Use structured keys + JSON + TTL for production
* Connect with Python using **redis-py**
* Tomorrow → we integrate **FastAPI + Redis caching**
