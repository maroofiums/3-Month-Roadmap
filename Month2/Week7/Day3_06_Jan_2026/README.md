# 🟦 Week 7 – Day 3: JWT in FastAPI

## 🎯 Day 3 Goal

By the end of today, you will:

* Create a **login endpoint**
* Generate a **JWT token**
* Protect routes using JWT
* Understand the **full auth flow**

⚠️ We’ll **NOT use a database today** — focus is auth logic.

---

## 1️⃣ What We Are Building Today

### Endpoints

* `POST /login` → returns JWT
* `GET /protected` → requires valid JWT

### Flow

```
User logs in
→ gets token
→ sends token in header
→ server validates token
→ access granted
```

---

## 2️⃣ Required Packages

Install these:

```bash
pip install fastapi uvicorn python-jose
```

---

## 3️⃣ Basic FastAPI App Setup

```python
from fastapi import FastAPI

app = FastAPI()
```

---

## 4️⃣ Fake User (No Database)

```python
fake_user = {
    "username": "admin",
    "password": "admin123"
}
```

🧠 This replaces DB **only for learning**

---

## 5️⃣ JWT Configuration

```python
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

⚠️ In real apps:

* Secret key → env variable
* Never hardcode

---

## 6️⃣ Create JWT Token Function

```python
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

🧠 This function:

* Adds expiry
* Signs payload
* Returns JWT

---

## 7️⃣ Login Endpoint (Token Generation)

```python
from fastapi import HTTPException

@app.post("/login")
def login(username: str, password: str):
    if username != fake_user["username"] or password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
```

### What’s happening?

* Credentials verified
* Token created
* Token returned to client

---

## 8️⃣ Token Extractor (OAuth2)

FastAPI provides this utility:

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
```

🧠 This:

* Extracts token from header
* `Authorization: Bearer <token>`

---

## 9️⃣ Get Current User (Token Validation)

```python
from fastapi import Depends

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
        return username
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
```

🧠 This function:

* Decodes JWT
* Verifies signature & expiry
* Extracts user identity

---

## 🔒 10️⃣ Protected Route

```python
@app.get("/protected")
def protected_route(user: str = Depends(get_current_user)):
    return {"message": f"Hello {user}, you are authenticated"}
```

🔥 Any request without valid JWT → **401 Unauthorized**

---

## 11️⃣ How to Test (Very Important)

### Step 1: Login

```
POST /login
```

Params:

```
username=admin
password=admin123
```

Response:

```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
```

---

### Step 2: Call Protected Route

Header:

```
Authorization: Bearer <access_token>
```

Endpoint:

```
GET /protected
```

Response:

```json
{
  "message": "Hello admin, you are authenticated"
}
```

---

## 12️⃣ Common Mistakes (Avoid ❌)

* Forgetting `Bearer`
* Using expired token
* Hardcoding secret in real apps
* Putting passwords in JWT

---

## 13️⃣ Mental Model (Remember This)

* Login → **create token**
* Token → **proof of identity**
* Protected route → **verify token**
* Depends() → **clean security**

---

## 🔑 Day 3 Summary / Tip

> JWT auth = **login once, verify everywhere**
> Today you built a **real auth system**, minus DB.
