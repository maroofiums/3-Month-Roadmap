# 🚀 1-Week Plan: Sanic + SQLModel Framework Prototype (Velox-like)


## 🟩 Day 1 — Framework Core (Sanic Basics)

### What you build

* Minimal **VeloxApp** wrapper around Sanic

### Tasks

* Learn **Sanic app lifecycle**
* Create core file:

```
velox/
 ├── __init__.py
 ├── app.py        # VeloxApp
```

### Concept

```python
class VeloxApp:
    def __init__(self):
        self.app = Sanic("VeloxApp")

    def run(self):
        self.app.run()
```

### Why this matters

* Tum Sanic ko **direct use nahi** kar rahe
* Tum **Sanic ko wrap** kar rahe ho → framework ban raha hai

✅ **Rule:** Framework = abstraction over framework

---

## 🟩 Day 2 — Routing Layer (Hello Route)

### Goal

User likhe:

```python
@app.route("/hello")
async def hello(request):
    return {"msg": "Hello Velox"}
```

### Tasks

* Create routing wrapper
* Auto JSON response

### Files

```
velox/
 ├── routing.py
```

### Logic

* `@route()` decorator
* Internally Sanic route register ho

### Advice

* Path params abhi skip karo
* Sirf **GET route** enough for prototype

---

## 🟩 Day 3 — Built-in ORM (SQLModel + SQLite)

### Goal

Framework ke sath **default database ready ho**

### Tasks

* Setup SQLModel + async engine
* Auto create `db.sqlite3`
* BaseModel inside framework

### Files

```
velox/
 ├── db.py
 ├── models.py
```

### Example

```python
engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3")
```

### Why SQLModel?

* Simple
* Type hints
* Future FastAPI-style feel
* Async support

⚠️ Django ORM avoid — async-first nahi

---

## 🟩 Day 4 — App Factory + Config System

### Goal

Framework user likhe:

```python
from velox import VeloxApp

app = VeloxApp()
```

### Tasks

* App factory pattern
* Load config (db path, debug)
* Auto DB init on startup

### Files

```
velox/
 ├── config.py
 ├── lifecycle.py
```

### Concept

* Framework handles startup
* User sirf routes likhe

This is **professional framework behavior**.

---

## 🟩 Day 5 — CLI Tool (Most Important Day)

### Goal

Command:

```bash
velox makeproject app
```

### Tasks

* Use `argparse` or `click`
* Create directory structure
* Auto-generate files

### Output Structure

```
app/
 ├── main.py
 ├── models.py
 ├── db.sqlite3
 ├── routes/
 │   └── hello.py
 └── config.py
```

### main.py auto-generated

```python
from velox import VeloxApp

app = VeloxApp()

@app.route("/hello")
async def hello(request):
    return {"msg": "Hello Velox"}

app.run()
```

🔥 This is where your framework feels **real**.

---

## 🟩 Day 6 — CLI Run Command

### Goal

```bash
velox run
```

### Tasks

* Detect `main.py`
* Call Sanic internally
* Support reload (optional)

### CLI commands

```bash
velox makeproject
velox run
velox version
```

### Advice

* Keep CLI **thin**
* Logic framework me ho

---

## 🟩 Day 7 — Cleanup + Public Release

### Tasks

* Rename things cleanly
* Add README:

  * What is Velox
  * How to install
  * How to create app
* Add architecture diagram
* Push to GitHub

### Repo structure

```
velox-framework/
 ├── velox/
 ├── cli.py
 ├── README.md
 └── pyproject.toml
```

---
