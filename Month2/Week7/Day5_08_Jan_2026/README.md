# 🟦 Week 7 – Day 5: Middleware Concept

## 🎯 Goal of Day 5

By the end of today, you will:

* Understand what **middleware** is
* Know the **request-response flow**
* Identify **common use cases**
* See **why FastAPI middleware is important for real apps**

---

## 1️⃣ What is Middleware?

Think of middleware as a **filter or guard** that runs **between the client request and the route handler**.

Flow:

```
Client Request → Middleware → Route → Middleware → Response → Client
```

* Middleware can **read/modify requests**
* Middleware can **read/modify responses**
* Runs for **all or selected routes**

---

## 2️⃣ Real-Life Analogy

* You go to a **restaurant**:

  * Middleware = **security guard + receptionist**
  * They check your ticket (auth), note time (logging), maybe limit number of people (rate limiting)
  * Then you go inside (route)

---

## 3️⃣ Why Middleware is Important

* Centralized logic → no repetition
* Can handle **global functionality**:

  * Logging
  * Authentication checks (optional)
  * Rate limiting
  * Header manipulation
* Scales better than putting the same code in every route

---

## 4️⃣ Middleware vs Dependency Injection (Quick Comparison)

| Feature    | Dependency (`Depends`)   | Middleware                    |
| ---------- | ------------------------ | ----------------------------- |
| Scope      | Route-specific           | Global / All routes           |
| Use-case   | Auth, DB, reusable logic | Logging, rate limit, headers  |
| Runs       | Before route function    | Before & after route function |
| Can modify | Can return value         | Can modify request/response   |

✅ Both can work together. Middleware = **global behavior**, DI = **per-route reusable logic**.

---

## 5️⃣ Example Middleware: Logging Requests

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Call the actual route
    response = await call_next(request)
    
    process_time = time.time() - start_time
    print(f"Path: {request.url.path} | Duration: {process_time:.2f}s")
    
    return response
```

### 🔍 What happens

1. Request comes in → logs start time
2. Route executes → `call_next(request)`
3. Response returned → logs duration
4. Finally returns response to client

---

## 6️⃣ Middleware Use Cases

| Use Case       | Example                                     |
| -------------- | ------------------------------------------- |
| Logging        | Track API requests & duration               |
| Authentication | Global token check before hitting any route |
| Rate Limiting  | Limit requests per IP                       |
| Headers        | Add security headers (CORS, HSTS)           |
| Error Handling | Catch unhandled exceptions globally         |

---

## 7️⃣ Things to Remember

* Middleware runs **for every request**
* Async middleware → use `await call_next(request)`
* Don’t put heavy logic here → slows all requests
* Middleware + Depends = powerful combo

---
