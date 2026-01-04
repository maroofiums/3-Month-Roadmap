# 🟦 WEEK 7 (Jan 4 – Jan 10)

## Authentication + Middleware (Backend Core Week)

### Why this week matters

* Week 6 → **Performance (Async)**
* Week 7 → **Security + Clean Architecture**

> A backend without authentication is **not production-ready**.

---

## 🔹 Day 1 – Authentication Basics (Jan 4)

### What is Authentication?

Authentication answers:

> **Who is the user?**

Without auth:

* Anyone can access APIs
* No user identity
* Security risk

With auth:

* User identity verified
* Protected endpoints
* Controlled access

---

### Token vs Session

#### Session-based Auth

* Server stores session data
* Client sends cookies
* Common in Django

❌ Not ideal for APIs

---

#### Token-based Auth (Modern APIs)

* Client stores token
* Token sent with every request
* Server stays stateless

✅ Best for:

* REST APIs
* Mobile apps
* SPA frontends

---

## 🔹 Day 2 – JWT Theory (Jan 5)

### What is JWT?

JWT = **JSON Web Token**

Format:

```
Header.Payload.Signature
```

#### Header

* Algorithm (HS256)
* Token type

#### Payload

* User data (id, email)
* Claims (exp, sub)

⚠️ Never store passwords in JWT

#### Signature

* Created using secret key
* Prevents tampering

---

### Why JWT?

* Stateless
* Scalable
* FastAPI friendly

---

## 🔹 Day 3 – JWT in FastAPI (Jan 6)

### Login Endpoint (Token Generation)

```python
from fastapi import FastAPI
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGORITHM = "HS256"

app = FastAPI()

@app.post("/login")
def login():
    payload = {
        "sub": "user_id",
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}
```

---

### Protected Route

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except:
        raise HTTPException(status_code=401)

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return {"user": user}
```

---

## 🔹 Day 4 – Dependency Injection (Jan 7)

### Why `Depends()` is powerful

* Clean code
* Reusable logic
* Centralized authentication

```python
@app.get("/items")
def read_items(user=Depends(get_current_user)):
    return {"user": user}
```

👉 One auth function → protects many routes

---

## 🔹 Day 5 – Middleware Concept (Jan 8)

### What is Middleware?

Middleware runs **between request and response**.

Flow:

```
Request → Middleware → Route → Middleware → Response
```

### Common use cases

* Logging
* Authentication
* Rate limiting
* Headers

---

## 🔹 Day 6 – Logging Middleware (Jan 9)

```python
import time
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    print(f"{request.url.path} - {duration:.2f}s")
    return response
```

✔ Used in real production systems

---

## 🔹 Day 7 – Secure API Project (Jan 10)

### 📌 Mini Project: Secure Todo API

Features:

* JWT authentication
* Protected CRUD routes
* Logging middleware

Structure:

```
app/
├── main.py
├── auth.py
├── models.py
├── routes.py
```

### Request flow

1. User logs in → receives JWT
2. Token sent in Authorization header
3. Protected endpoints validate token
4. Middleware logs all requests

---

## 🔑 Week 7 Key Takeaways

1. Authentication is mandatory
2. JWT provides stateless security
3. `Depends()` keeps code clean
4. Middleware handles global logic
5. Never expose secrets
