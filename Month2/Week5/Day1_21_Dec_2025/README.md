# 🟦 Day 1 – REST + FastAPI Basics (Deep but Simple)

## 🎯 Day 1 Goal

By end of today:

* REST ka **clear mental model**
* FastAPI ka **hello-world + health API**
* Swagger UI ka **proper use**

---

## 1️⃣ REST kya hota hai? (No bookish talk)

**REST = ek style hai APIs design karne ka**

Simple words:

> *“Client kya request karega, aur server kaise respond karega”*

Example (real life):

* Zomato app → request
* Server → response (food list)

---

### REST ke 3 golden rules (Day 1 ke liye enough)

1. **URL = resource**

   * `/users`
   * `/users/5`

2. **Method = action**

   * GET → laao
   * POST → banao
   * PUT → update
   * DELETE → hatao

3. **Response = JSON + status code**

---

## 2️⃣ FastAPI kya hai aur kyun use karte hain?

FastAPI = **modern Python web framework** for APIs

Why industry likes it:

* 🚀 Fast (async support)
* 🧠 Smart (auto validation)
* 📘 Swagger docs auto

Honest advice:

> Django/Flask ke baad FastAPI seekhna **backend maturity** ka sign hai.

---

## 3️⃣ Environment Setup (Clean way)

### Step 1: Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate
```

---

### Step 2: Install FastAPI

```bash
pip install fastapi uvicorn
```

---

## 4️⃣ First FastAPI App (Heart of Day 1)

### `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Backend World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
```

---

## 5️⃣ Run Server (Important Concept)

```bash
uvicorn main:app --reload
```

### Breakdown (must understand)

* `main` → file name
* `app` → FastAPI object
* `--reload` → auto restart on code change

If yeh samajh aa gaya → backend basics strong 💪

---

## 6️⃣ Testing (Swagger = Tumhara Weapon)

Open:
👉 `http://127.0.0.1:8000/docs`

What you’ll see:

* Interactive API playground
* Try endpoints without Postman

### Test:

* GET `/`
* GET `/health`

---

## 7️⃣ Request → Response Flow (MOST IMPORTANT)

```text
Browser / Client
        ↓
    Endpoint (/health)
        ↓
     Python function
        ↓
    JSON response
```

Think of endpoint as:

> *“Normal Python function, but internet se call ho rahi hai”*

---

## 8️⃣ Common Beginner Mistakes (Avoid karo)

❌ Flask mindset (global variables everywhere)
❌ Ignoring status codes
❌ Writing logic inside route directly (we’ll fix later)

✅ Clean functions
✅ Simple return JSON
✅ Understand flow, not copy code

---

## 🧠 Day 1 Mini Practice (DO THIS)

1. Add new endpoint:

```python
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
```

Test in browser:

```
/hello/Maroof
```

2. Add query param:

```python
@app.get("/greet")
def greet(name: str = "Guest"):
    return {"greet": name}
```

---

## 🔑 Day 1 Summary (Yaad rakhna)

* REST = rules
* FastAPI = framework
* Endpoint = function exposed to internet
* Swagger = testing tool
* `uvicorn main:app` = server ka dil ❤️
