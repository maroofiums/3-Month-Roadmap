## 🔹 Day 4 – Dependency Injection (FastAPI)

### 🔑 Core Idea

**Dependency Injection (DI)** means:

> “Don’t repeat logic again and again — write it once and *inject* it wherever needed.”

FastAPI makes this **super clean** using `Depends()`.

---

## 1️⃣ Why Dependency Injection is needed (Real Problem)

Imagine this 👇

You have:

* 10 protected routes
* Each route needs:

  * Read JWT token
  * Verify token
  * Get current user

❌ **Bad approach**

```python
def route1():
    decode token
    verify token
    get user

def route2():
    decode token
    verify token
    get user
```

👉 Repetition
👉 Hard to maintain
👉 Bug-prone

---

## 2️⃣ Dependency Injection = Reusable Guard

We write **auth logic once**
Then FastAPI automatically runs it before the route.

That logic becomes a **dependency**.

---

## 3️⃣ Basic Dependency Example (Simple First)

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def common_logic():
    return "Hello from dependency"

@app.get("/test")
def test(dep=Depends(common_logic)):
    return {"msg": dep}
```

### 🔍 What happened?

* `common_logic()` runs automatically
* Its return value is injected into `dep`

---

## 4️⃣ Real Auth Dependency: `get_current_user`

This is the **heart of JWT auth**.

### Step-by-step flow:

1. Read token from request
2. Decode JWT
3. Validate user
4. Allow or block request

---

## 5️⃣ Auth Dependency Code (Core Concept)

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "secret"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401)

        return username

    except jwt.PyJWTError:
        raise HTTPException(status_code=401)
```

📌 This function:

* Runs **before route**
* Blocks request if token invalid
* Returns user if valid

---

## 6️⃣ Protecting a Route (Magic Line)

```python
@app.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {"msg": f"Welcome {user}"}
```

### 🧠 Think like this:

> “FastAPI, before entering this route, make sure user is valid.”

---

## 7️⃣ Why Dependency Injection is POWERFUL 🔥

✅ Clean code
✅ Reusable
✅ Central auth logic
✅ Easy testing
✅ Easy upgrade (DB later, roles later)

This is why **FastAPI is production-grade**.

---

## 8️⃣ Important Clarification (Your Confusion)

### ❓ Do we need DB for learning auth?

**NO.**

Right now:

* We focus on **JWT + flow**
* User can be **fake / hardcoded**

Later:

* Same dependency → add DB inside it
* Routes stay untouched 😎

👉 That’s the **real power of DI**

---

## ⚠️ Common Mistakes to Avoid

❌ Writing auth logic inside every route
❌ Not using `Depends()`
❌ Mixing DB logic inside route functions

---

## ✅ Best Practice 

* Auth logic → Dependency
* Routes → Business logic only
* DB → Inside dependency (later)

---