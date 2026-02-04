# Month3 Week11 Day 4 (Wed) — Rate Limiter

## What to Learn

* Why rate limiting is important
* Fixed Window vs Sliding Window
* Per-user rate limiting

---

## What is Rate Limiting?

Rate limiting restricts how many requests a user can make within a specific time window.

Purpose:

* Protect server from overload
* Prevent abuse and bots
* Ensure fair usage for all users

Common examples:

* Login API: 5 requests per minute
* Public API: 100 requests per minute
* AI APIs: token or request-based limits

---

## Core Idea

User → Request Count → Time Window → Allow or Block

---

## Types of Rate Limiting

### Fixed Window

* Time window is fixed (for example 60 seconds)
* Counter resets after window ends

Example:

* Max 10 requests per 60 seconds
* Counter resets every minute

Pros:

* Simple
* Easy to implement

Cons:

* Edge case at window boundary

---

### Sliding Window

* Time moves with each request
* More accurate

Pros:

* Smooth and fair

Cons:

* Complex implementation

Note: Fixed Window is enough for beginners and interviews.

---

## Per-User Rate Limiting

Each user has a separate counter.

Example Redis keys:

* user:192.168.1.1
* user:192.168.1.2

This avoids one user affecting others.

---

## Mini Implementation (FastAPI + Redis)

### Requirements

```bash
pip install fastapi uvicorn redis
```

---

## Project Structure

```
rate_limiter/
│
├── main.py
├── README.md
```

---

## main.py

```python
from fastapi import FastAPI, HTTPException, Request
import redis

app = FastAPI()

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

RATE_LIMIT = 10
WINDOW_SIZE = 60

@app.get("/data")
def get_data(request: Request):
    user_id = request.client.host
    key = f"user:{user_id}"

    count = redis_client.incr(key)

    if count == 1:
        redis_client.expire(key, WINDOW_SIZE)

    if count > RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Try again later."
        )

    return {
        "message": "Request successful",
        "request_count": count
    }
```

---

## Logic Explanation

1. Identify user using IP address
2. Increment request count in Redis
3. Set expiry only on first request
4. Block user if count exceeds limit
5. Return HTTP 429 error if blocked

---

## How to Run

Start Redis:

```bash
redis-server
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Test in browser or Postman:

```
http://127.0.0.1:8000/data
```

After 10 requests in 60 seconds, response will be blocked.

---

## Best Practices

* Use Redis instead of in-memory counters
* Apply limits per user or API key
* Always set expiry on counters
* Return proper HTTP status codes

---

## Avoid

* No expiry on Redis keys
* Global limits for all users
* Storing counters in application memory

---

## Summary

* Rate limiter controls request frequency
* Redis INCR + EXPIRE is the core pattern
* Fixed window is simple and effective
* HTTP 429 means Too Many Requests

---