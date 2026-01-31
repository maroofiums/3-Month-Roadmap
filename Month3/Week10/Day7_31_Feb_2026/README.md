# **Week 10 – Day 7**

**Goal:**

* FastAPI basics
* ML model serving
* Async endpoints
* Redis caching
* Testing & Documentation

Time: **2 hours max** – short, focused, practical review

---

## **Hour 1: FastAPI Basics Review**

### 1️⃣ Project Structure

```text
ml_api/
 ├─ main.py
 ├─ models.py   # ML model load
 ├─ schemas.py  # Pydantic models
 ├─ utils.py    # caching, helpers
 └─ requirements.txt
```

### 2️⃣ Key FastAPI Features

* GET vs POST endpoints
* Path vs Query parameters
* Pydantic validation → type safety
* Auto docs → `/docs` & `/redoc`

### Mini Practice

* Create GET `/ping` → returns `{"status":"alive"}`
* Test POST `/sum` with JSON input → validate errors automatically

---

## **Hour 2: ML Model Serving + Async + Caching**

### 1️⃣ Load ML Model

```python
import joblib
model = joblib.load("titanic_model.pkl")
```

### 2️⃣ Basic Prediction Endpoint

```python
@app.post("/predict")
def predict(data: Passenger):
    features = [[data.Age, data.Fare, data.Sex, data.Pclass]]
    pred = model.predict(features)
    return {"prediction": int(pred[0])}
```

### 3️⃣ Async Endpoint

```python
@app.post("/predict_async")
async def predict_async(data: Passenger):
    features = [[data.Age, data.Fare, data.Sex, data.Pclass]]
    pred = model.predict(features)
    return {"prediction": int(pred[0])}
```

### 4️⃣ Redis Caching (Optimization)

```python
import redis, json
r = redis.Redis(host="localhost", port=6379, db=0)

@app.post("/predict_cached")
async def predict_cached(data: Passenger):
    key = f"{data.Age}_{data.Fare}_{data.Sex}_{data.Pclass}"
    cached = r.get(key)
    if cached:
        return {"prediction": int(json.loads(cached)), "cached": True}
    
    features = [[data.Age, data.Fare, data.Sex, data.Pclass]]
    pred = int(model.predict(features)[0])
    r.set(key, json.dumps(pred), ex=60)
    return {"prediction": pred, "cached": False}
```

### 5️⃣ Testing & Docs

* Postman / curl test endpoints
* Check cached vs fresh predictions
* Auto docs at `/docs` → great for **GitHub showcase**

---
