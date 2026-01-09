# 🟦 Day6 -- Logging Middleware in FastAPI

### **Goal**

* Log **request path**
* Log **duration of request**
* Log **username from JWT** (if available)
* Minimal, reusable, production-friendly

---

## 1️⃣ Basic Async Logging Middleware

```python
import time
from fastapi import Request

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    
    # Process request
    response = await call_next(request)
    
    # Calculate duration
    duration = time.time() - start_time
    
    # Log path and duration
    print(f"Path: {request.url.path} | Duration: {duration:.2f}s")
    
    return response
```

✅ This is **all you need** for basic logging.

---

## 2️⃣ Optional: Log Username (if JWT token present)

If you already have **JWT auth**:

```python
from .auth import get_current_user  # your auth dependency

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    
    # Default user if no token
    username = "anonymous"
    
    auth_header = request.headers.get("Authorization")
    if auth_header:
        try:
            token = auth_header.split(" ")[1]  # Bearer token
            username = await get_current_user(token)
        except:
            username = "invalid_token"
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    print(f"User: {username} | Path: {request.url.path} | Duration: {duration:.2f}s")
    
    return response
```

💡 Notes:

* `get_current_user` is the **JWT validation function** from Day 3/4
* Middleware logs **user identity** if available
* Doesn’t block requests — it only logs

---

## 3️⃣ How to Add Middleware to FastAPI

```python
from fastapi import FastAPI
from .middleware import logging_middleware  # the file you created

app = FastAPI()

# Add middleware
app.middleware("http")(logging_middleware)
```

---

## 4️⃣ Example Console Output

```
User: admin | Path: /items | Duration: 0.02s
User: anonymous | Path: /public | Duration: 0.01s
User: invalid_token | Path: /protected | Duration: 0.03s
```

---

## 5️⃣ Best Practices

1. Middleware = **lightweight**

   * Don’t put heavy DB queries here → slows **all requests**
2. Log **only what you need** → sensitive info? don’t log passwords
3. Combine with DI (`Depends`) for auth checks
4. Later → can add **request ID** to track logs for production

---
