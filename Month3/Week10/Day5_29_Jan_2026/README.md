# Day 5 – Test Iris ML API with Redis

**Objective:**  
Test the Iris ML API built with **FastAPI** and **Redis caching**, ensuring correct predictions and cache functionality.

---

## 🧩 Project Overview

- ML Model: **RandomForestClassifier** trained on Iris dataset
- API Framework: **FastAPI**
- Caching: **Redis** for repeated predictions
- Features:
  - `/predict` endpoint
  - Input validation via **Pydantic**
  - Cache check → Redis → ML model

---

## 🏗 Project Structure

```

iris_api/
│
├── app/
|   ├──Test
|   |  └── main.py
│   ├── main.py        # FastAPI app
│   ├── model.py       # Load & predict ML model
│   ├── schema.py      # Request/Response validation
│   └── redis_cache.py # Redis client
│
├── train.py           # Train and save model
├── model.pkl          # Saved ML model
├── requirements.txt
└── README.md

````

---

## ⚡ Installation Steps

1. Clone repository:
```bash
git clone <repo_url>
cd iris_api
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start Redis server (ensure it is running):

```bash
redis-server
```

4. Train ML model (first time only):

```bash
python train.py
```

5. Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testing the API

### 1️⃣ Swagger UI (Recommended)

* Open: `http://127.0.0.1:8000/docs`
* Go to `POST /predict`
* Click **Try it out**
* Example input:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

* Click **Execute**
* Response:

```json
{
  "source": "ml_model",
  "prediction": 0
}
```

* Repeat same input → `"source": "redis_cache"` confirms caching works

---

### 2️⃣ Python Script

```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "sepal_length": 6.0,
    "sepal_width": 3.0,
    "petal_length": 4.8,
    "petal_width": 1.8
}

response = requests.post(url, json=data)
print(response.json())
```

* Expected Output:

```json
{"source": "ml_model", "prediction": 2}
```

* Repeat same input → `"source": "redis_cache"`

---

### 3️⃣ cURL (Terminal)

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

---

## 🔍 Notes & Best Practices

* Ensure **Redis server** is running before testing
* Test **Swagger UI first**, then scripts for automation
* Redis caching improves repeated prediction performance
* For production:

  * Map prediction index → Iris species names
  * Use Redis expiry (`setex`) to manage cache memory
  * Dockerize the project for deployment

---