# **Week 10 – ML API Integration**

**Goal:** Serve ML models via **FastAPI**, **async endpoints**, and **Redis caching** for speed.

---

## **Day 1 – Mon (25 Jan) → FastAPI Basics**

**Focus:** Setup FastAPI project & create first endpoint

### **Tasks**

1. Install FastAPI & uvicorn

```bash
pip install fastapi uvicorn
```

2. Create project structure:

```
ml_api/
  main.py
```

3. Create a simple endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML API is running!"}
```

4. Run server

```bash
uvicorn main:app --reload
```

* Open `http://127.0.0.1:8000` → should return JSON message

### **Tip:**

* `--reload` → auto-reload code
* FastAPI docs auto available at `http://127.0.0.1:8000/docs`

---

## **Day 2 – Tue (26 Jan) → Serve ML Model**

**Focus:** Load `joblib` ML model & create `/predict` endpoint

### **Tasks**

1. Save your Week 9 model (`joblib.dump(model, "model.pkl")`)
2. Load model in FastAPI

```python
import joblib
model = joblib.load("model.pkl")
```

3. Create prediction endpoint

```python
from pydantic import BaseModel

class Passenger(BaseModel):
    Age: float
    Fare: float
    Sex: int
    Pclass: int

@app.post("/predict")
def predict(passenger: Passenger):
    data = [[passenger.Age, passenger.Fare, passenger.Sex, passenger.Pclass]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
```

### **Tips**

* Always use **Pydantic models** → input validation
* Prevent wrong types or missing fields

---

## **Day 3 – Wed (27 Jan) → Async Endpoints**

**Focus:** Use `async def` to improve response time for multiple requests

### **Tasks**

```python
@app.post("/predict_async")
async def predict_async(passenger: Passenger):
    data = [[passenger.Age, passenger.Fare, passenger.Sex, passenger.Pclass]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
```

### **Tips**

* Async endpoints → non-blocking → multiple requests handle easily
* For ML model, small sync calls are ok, but async helps if DB + caching included

---

## **Day 4 – Thu (28 Jan) → Redis Caching**

**Focus:** Cache repeated predictions to avoid recomputation

### **Tasks**

1. Install Redis & Python client

```bash
pip install redis
```

2. Connect Redis

```python
import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0)
```

3. Add caching to `/predict` endpoint

```python
@app.post("/predict_cached")
async def predict_cached(passenger: Passenger):
    key = f"{passenger.Age}_{passenger.Fare}_{passenger.Sex}_{passenger.Pclass}"
    
    cached = r.get(key)
    if cached:
        return {"prediction": int(json.loads(cached)), "cached": True}
    
    data = [[passenger.Age, passenger.Fare, passenger.Sex, passenger.Pclass]]
    prediction = int(model.predict(data)[0])
    
    r.set(key, json.dumps(prediction), ex=60)  # cache expires in 60s
    return {"prediction": prediction, "cached": False}
```

### **Tips**

* Cache reduces repeated ML computation → **faster API**
* `ex=60` → cache expiry in seconds

---

## **Day 5 – Fri (29 Jan) → Test API**

**Focus:** Use Postman / curl to test all endpoints

### **Tasks**

* Test GET `/`
* Test POST `/predict` with JSON body:

```json
{
  "Age": 22,
  "Fare": 7.25,
  "Sex": 1,
  "Pclass": 3
}
```

* Test POST `/predict_cached` → check cached vs new response

### **Tips**

* Always validate responses
* Handle errors gracefully with `try-except`

---

## **Day 6 – Sat (30 Jan) → Mini Project**

**Focus:** Build **ML Prediction API (Titanic/Iris)** with async + caching

### **Tasks**

* Combine all features:

  * `/predict` → simple
  * `/predict_async` → async
  * `/predict_cached` → caching
* Push project to GitHub
* Include requirements.txt

```bash
pip freeze > requirements.txt
```

### **Tips**

* Modular code → `main.py`, `models.py`, `schemas.py`
* Always test before pushing

---

## **Day 7 – Sun (31 Jan) → Docs & README**

**Focus:** Document endpoints & usage

### **Tasks**

* FastAPI auto docs → `http://127.0.0.1:8000/docs`
* Write README.md:

  * Project description
  * Installation steps
  * Endpoint usage examples
* Add flow diagram:

```
[Client] → [FastAPI] → [ML Model] → [Redis Cache]
```

### **Tips**

* Good docs + diagram = professional project
* Helps in interviews + GitHub showcase
