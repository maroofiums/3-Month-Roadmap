from fastapi import FastAPI
from schemas import IrisInput
from model import predict_iris
from redis_cache import redis_client
import json

app = FastAPI(title="Iris ML API with Redis")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris ML API"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: IrisInput):

    key = json.dumps(data.dict(), sort_keys=True)

    cached_result = redis_client.get(key)
    if cached_result:
        return {
            "source": "redis_cache",
            "prediction": int(cached_result)
        }

    features = list(data.dict().values())
    result = predict_iris(features)

    redis_client.set(key, result)

    return {
        "source": "ml_model",
        "prediction": result
    }
