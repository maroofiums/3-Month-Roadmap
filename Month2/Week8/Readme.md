# 🟦 WEEK 8 — Redis + Production Mini Project

**Goal:** FastAPI ko *production-ready* banana 🚀

---

## 🟩 Day 1 – Caching Concept (11 Jan)

### ❓ Why Cache?

Simple words mein:

> **Cache = short-term memory for your app**

#### 🔹 Fast Response

* DB se data lana **slow** hota hai
* Cache (Redis) RAM mein hota hai → **super fast**

Example:

```text
Without cache:
Client → API → Database → API → Client (slow)

With cache:
Client → API → Redis → Client (fast ⚡)
```

#### 🔹 Less DB Load

* Same GET request 1000 baar aaye?
* DB 1000 baar hit nahi hona chahiye ❌
* Redis se serve karo ✅

💡 **Honest advice:**

> Cache tab use karo jab **same data baar baar read** hota ho
> CRUD ke har endpoint pe cache lagana ❌ (galti hoti hai)

---

## 🟩 Day 2 – Redis Basics (12 Jan)

### 🔹 Key → Value Store

Redis bilkul dictionary jaisa hai:

```text
"user:1" → "{id:1, name:'Ali'}"
```

Python example:

```python
await redis.set("user:1", user_json)
data = await redis.get("user:1")
```

### 🔹 TTL (Time To Live)

TTL ka matlab:

> Data kitni dair cache mein rahe

```python
await redis.set("users:all", data, ex=60)
```

⏱️ After 60 seconds → auto delete

💡 **Best Practice**

* Short TTL for dynamic data (30–120 sec)
* Long TTL for static data (5–10 min)

Avoid ❌:

* Infinite TTL (stale data bug)

---

## 🟩 Day 3 – Redis with FastAPI (13 Jan)

### 🎯 Cache GET Responses

Rule:

> **Only cache GET, never POST/PUT/DELETE**

Flow:

```text
Request → Check Redis
  ├─ If found → return cached response
  └─ If not → DB → Save to Redis → return
```

Example logic:

```python
cache_key = "users:all"

cached = await redis.get(cache_key)
if cached:
    return cached

data = get_users_from_db()
await redis.set(cache_key, data, ex=60)
return data
```

💡 **Important Tip**

* Update/Delete ke baad related cache **invalidate** karo

```python
await redis.delete("users:all")
```

---

## 🟩 Day 4 – Rate Limiting (14 Jan)

### ❓ Why Rate Limit?

Prevent:

* Abuse
* Bots
* DDoS

Example:

```text
Max 5 requests / minute / IP
```

### Redis + Rate Limit Logic

```text
Key: rate:IP
Value: request_count
TTL: 60 sec
```

Pseudo flow:

```python
count = await redis.incr(key)
if count == 1:
    await redis.expire(key, 60)

if count > 5:
    raise 429 Too Many Requests
```

💡 **Honest Advice**

* Rate limit **login**, **signup**, **public APIs**
* Internal admin APIs pe soft limits

---

## 🟩 Day 5 – Final Mini Project Start (15 Jan)

### 📌 Final Project Scope (Perfect for CV)

#### Features:

✅ Async CRUD API
✅ JWT Authentication
✅ Redis caching (GET)
✅ Redis rate limiting
✅ Clean folder structure

### Suggested Structure:

```text
app/
 ├─ main.py
 ├─ core/
 │   ├─ config.py
 │   ├─ security.py
 ├─ db/
 │   ├─ database.py
 ├─ routes/
 │   ├─ auth.py
 │   ├─ users.py
 ├─ services/
 │   ├─ cache.py
 │   ├─ rate_limit.py
```

💡 **Best Practice**

* Redis logic **separate service file** mein rakho
* main.py ko clean rakho

---

## 🟩 Day 6 – Testing + Cleanup (16 Jan)

### 🧪 Test:

* JWT protected routes
* Cache hit/miss
* Rate limit trigger
* Invalid token cases

### 🔧 Edge Cases:

* Cache not available → app crash ❌
  → try/except + fallback DB
* Redis down → degrade gracefully

💡 **Production Tip**

> App should work **even if Redis fails**

---

## 🟩 Day 7 – README + GitHub (17 Jan)

### README Must Include:

#### 🔹 How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### 🔹 Features

* JWT Auth
* Redis Cache
* Rate Limiting

#### 🔹 Tech Stack

* FastAPI
* PostgreSQL / SQLite
* Redis
* JWT

💡 **GitHub Tip**

* Clear commits
* Proper README = recruiter impressed 😎

---

