from fastapi import FastAPI
from app.model import predict_churn
from app.schemas import ChurnRequest

app = FastAPI(title="Customer Churn Prediction API")

@app.get("/")
async def home():
    return {"message": "Customer Churn Prediction API is running!"}

@app.post("/predict")
async def predict(request: ChurnRequest):
    data = request.dict()
    result = predict_churn(data)
    return result
