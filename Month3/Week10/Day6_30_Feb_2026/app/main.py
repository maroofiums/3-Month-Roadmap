from fastapi import FastAPI
from pathlib import Path
import pickle
import pandas as pd
from app.models import TitanicInput, TitanicOutput

app = FastAPI(title="Titanic Survival Predictor")

BASE_PATH = Path(__file__).parent
MODEL_DIR = BASE_PATH / "Model"
MODEL_PATH = MODEL_DIR / "titanic_model.pkl"
FEATURES_PATH = MODEL_DIR / "titanic_features.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(FEATURES_PATH, "rb") as f:
    feature_cols = pickle.load(f)

@app.post("/predict", response_model=TitanicOutput)
def predict(data: TitanicInput):
    df = pd.DataFrame([data.dict()], columns=feature_cols)
    prediction = model.predict(df)[0]
    return {"survived": int(prediction)}
