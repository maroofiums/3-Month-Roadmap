# **Week 10 – Day 1 (25 Jan) → FastAPI Basics**

**Goal:**

* Setup FastAPI project
* Create first endpoint
* Run server locally & understand request flow

---

## ⏱️ **Time-Sliced Plan (2–3 hours)**

---

### **Hour 1: Setup & Project Structure**

1️⃣ **Install FastAPI & Uvicorn**

```bash
pip install fastapi uvicorn
```

2️⃣ **Project folder structure**

```
ml_api/
  main.py
```

3️⃣ **Create first FastAPI app**

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML API is running!"}
```

4️⃣ **Run server**

```bash
uvicorn main:app --reload
```

* Open `http://127.0.0.1:8000` → should return `{"message": "ML API is running!"}`

✅ **Tip:**

* `--reload` → auto-reload changes
* FastAPI docs available at `http://127.0.0.1:8000/docs`

---

### **Hour 2: Learn Basic Endpoints**

1️⃣ **GET endpoint with parameter**

```python
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
```

Test:
`http://127.0.0.1:8000/hello/Maroof` → `{"message": "Hello, Maroof!"}`

---

2️⃣ **Query parameter**

```python
@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"sum": a + b}
```

Test:
`http://127.0.0.1:8000/sum?a=5&b=3` → `{"sum": 8}`

---

### **Hour 3: POST Endpoint & Input Validation**

1️⃣ **Install Pydantic** (already comes with FastAPI)

2️⃣ **Create POST endpoint**

```python
from pydantic import BaseModel

class InputData(BaseModel):
    x: int
    y: int

@app.post("/multiply")
def multiply(data: InputData):
    return {"result": data.x * data.y}
```

Test via **Postman / curl**

```bash
curl -X POST "http://127.0.0.1:8000/multiply" -H "Content-Type: application/json" -d '{"x":4,"y":5}'
```

Output: `{"result":20}`

---
