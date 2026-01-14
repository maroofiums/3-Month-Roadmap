# 🟦 DAY 4 – RATE LIMITING (Redis + FastAPI)

## 🔐 Why Rate Limiting?

Simple words mein:

> **Same user ko zyada requests bhejnay se rokna**

### Prevents:

* Abuse
* DDoS
* Brute-force login attempts
* Free API misuse

Real world example:

* ❌ Unlimited calls → server crash
* ✅ 5 requests / 10 seconds → safe

---

## 🧠 Concept First (Very Important)

We use **Redis counters + TTL**

Logic:

1. User hits API
2. Redis counter increment
3. If counter > limit → block
4. TTL auto reset

Redis key example:

```
rate_limit:127.0.0.1
```

---

# 📁 Project Structure

```
rate_limit_api/
│
├── main.py
├── redis_client.py
├── rate_limiter.py
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

---

## 2️⃣ redis_client.py

```python
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)
```

---

## 3️⃣ rate_limiter.py

👉 **Core logic yahan hai**

```python
from fastapi import Request, HTTPException
from redis_client import redis_client

RATE_LIMIT = 5        # requests
TIME_WINDOW = 10      # seconds


def rate_limiter(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    current_count = redis_client.get(key)

    if current_count is None:
        # First request
        redis_client.set(key, 1, ex=TIME_WINDOW)
        return

    if int(current_count) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Try again later."
        )

    redis_client.incr(key)
```

---

### 🔍 Logic Breakdown (Important)

* `set(key, 1, ex=10)` → first request
* `incr(key)` → next requests
* Redis TTL auto reset after 10 sec
* No manual cleanup needed ✅

---

## 4️⃣ main.py

```python
from fastapi import FastAPI, Depends, Request
from rate_limiter import rate_limiter

app = FastAPI(title="FastAPI Rate Limiting")


@app.get("/public")
def public_api(request: Request, _=Depends(rate_limiter)):
    return {
        "message": "You are within rate limit"
    }
```

---

## 🧪 How to Test

### Run Redis

```bash
redis-server
```

### Run FastAPI

```bash
uvicorn main:app --reload
```

### Hit endpoint quickly (browser / Postman)

```
GET /public
```

After **5 requests in 10 seconds** 👇

```json
{
  "detail": "Too many requests. Try again later."
}
```

Status Code:

```
429 Too Many Requests
```

🔥 Real-world behavior achieved.

---

## 🧠 What You Learned Today

✔ Redis counters
✔ TTL-based limits
✔ FastAPI Dependencies
✔ IP-based protection

---

## ❌ Common Mistakes (Avoid)

* ❌ No TTL → permanent block
* ❌ Using DB for rate limiting
* ❌ Applying to every endpoint blindly
* ❌ Hard-coding limits everywhere

---

## ✅ Best Practices

* Different limits for:

  * Login
  * Public APIs
  * Authenticated users
* Use:

  ```
  rate_limit:user_id
  rate_limit:ip
  ```

---