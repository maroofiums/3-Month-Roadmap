# 🧠 Week 11 (1 Feb – 7 Feb) → **System Design Lite**

**Goal:** Scalable APIs + databases ka *thinking mindset* develop karna
⏱ Daily Time: **2–3 hours** (samajhne pe focus, coding minimal but meaningful)

---

## 🟢 Day 1 (Sun) — **Database Indexing (Foundation Day)**

### 📌 What to Learn

* Index kya hota hai (real-life example: book index 📖)
* **B-Tree Index**
* **Hash Index**
* Primary key vs Secondary index
* Composite index (multiple columns)

### 🧠 Simple Explanation

> Index = database ka shortcut
> Without index → DB har row scan karta (slow)
> With index → directly required data

### 🔧 Hands-on

```sql
CREATE INDEX idx_email ON users(email);
```

* PostgreSQL / MySQL example
* Query explain samjho:

```sql
EXPLAIN SELECT * FROM users WHERE email='a@b.com';
```

### ✅ Best Practice

* Index **frequently queried fields**
* WHERE, JOIN, ORDER BY ke columns

### ❌ Avoid

* Har column pe index (write slow ho jata)
* Low-cardinality fields (gender, status)

### 🎯 Output

* Notes + 1 diagram (table → index → lookup)

---

## 🟢 Day 2 (Mon) — **Sharding Basics**

### 📌 What to Learn

* Vertical vs Horizontal scaling
* Sharding kya hoti hai
* Shard key concept

### 🧠 Example

Users table:

* Shard 1 → user_id 1–1000
* Shard 2 → user_id 1001–2000

### 🔧 Hands-on (Conceptual)

* Draw shard diagram
* Decide shard key:

  * user_id ✅
  * email ❌ (change ho sakta)

### ✅ Best Practice

* Shard key **immutable** hona chahiye
* Even data distribution

### ❌ Avoid

* Hot shards (ek shard pe zyada traffic)

### 🎯 Output

* 2 diagrams: vertical vs horizontal

---

## 🟢 Day 3 (Tue) — **Queue Basics (Very Important)**

### 📌 What to Learn

* Queue kya hoti hai
* Producer vs Consumer
* Async processing kyun use hota

### 🧠 Real-Life Example

> Order place → response turant
> Email / notification → background

### 🔧 Mini Code (Redis Queue)

```python
import redis
r = redis.Redis()

r.lpush("tasks", "send_email")
task = r.rpop("tasks")
```

### ✅ Best Practice

* Heavy tasks queue mein bhejo
* API fast rakho

### ❌ Avoid

* Queue ko direct user response se block karna

### 🎯 Output

* Producer–Consumer flow diagram

---

## 🟢 Day 4 (Wed) — **Rate Limiter**

### 📌 What to Learn

* Rate limiting kyun zaroori
* Fixed window vs Sliding window
* Per-user limit

### 🔧 Mini Implementation (FastAPI + Redis)

```python
key = f"user:{user_id}"
count = redis.incr(key)
redis.expire(key, 60)
```

### 🧠 Logic

* 60 sec mein max 10 requests
* Zyada → 429 error

### ✅ Best Practice

* Redis use karo (fast)
* Per-IP / per-user limit

### ❌ Avoid

* Hardcoding limits everywhere

### 🎯 Output

* Working rate-limited endpoint

---

## 🟢 Day 5 (Thu) — **URL Shortener (Mini System Design Project)**

### 📌 Components

* API
* Database
* Index
* (Optional) Queue

### 🧠 DB Design

```text
id | short_code | long_url | created_at
```

### 🔧 API Endpoints

* POST /shorten
* GET /{short_code}

### ✅ Best Practice

* short_code indexed
* collision handling

### ❌ Avoid

* Over-engineering (keep simple)

### 🎯 Output

* System diagram + schema

---

## 🟢 Day 6 (Fri) — **Notification System**

### 📌 What to Learn

* Async notification delivery
* Queue-based design

### 🔧 Flow

1. API request
2. Push task to queue
3. Worker sends notification

### 🧠 Example

* Email
* SMS
* In-app notification

### ✅ Best Practice

* Retry mechanism
* Idempotent workers

### ❌ Avoid

* Notification fail hone pe API fail karna

### 🎯 Output

* Queue + worker diagram

---

## 🟢 Day 7 (Sat) — **System Design Diagrams + Revision**

### 📌 What to Do

* Revise:

  * Index
  * Sharding
  * Queue
  * Rate limiting
* Draw **1 complete architecture**

### 🧠 Diagram Should Include

* Client
* API (FastAPI)
* DB (Indexed)
* Redis (Cache + Rate limit)
* Queue + Worker

### 📂 GitHub

* `/diagrams/`
* `/notes/`
* README.md with explanation

---
