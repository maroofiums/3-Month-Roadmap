from fastapi import FastAPI
from schemas import IrisInput
from model import predict_iris
from redis_cache import redis_client
import json

app = FastAPI(title="Iris ML API with Redis")

@app.post("/predict")
def predict(data: IrisInput):

    # Convert input to key
    key = json.dumps(data.dict(), sort_keys=True)

    # Check cache
    cached_result = redis_client.get(key)
    if cached_result:
        return {
            "source": "redis_cache",
            "prediction": int(cached_result)
        }

    # ML prediction
    features = list(data.dict().values())
    result = predict_iris(features)

    # Save to Redis
    redis_client.set(key, result)

    return {
        "source": "ml_model",
        "prediction": result
    }
