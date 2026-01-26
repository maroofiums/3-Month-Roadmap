import joblib
import pandas as pd

# Load artifacts
model = joblib.load("churn_model.pkl")
top_features = joblib.load("top_features.pkl")
le = joblib.load("label_encoder.pkl")

def preprocess_input(data: dict):
    """
    Convert input JSON to DataFrame, handle encoding, keep top features.
    """
    df = pd.DataFrame([data])

    # Label encoding for binary columns
    for col in df.columns:
        if col in ["gender", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]:
            df[col] = le.transform(df[col])

    # Ensure columns match top_features
    missing_cols = [c for c in top_features if c not in df.columns]
    for c in missing_cols:
        df[c] = 0

    df = df[top_features]

    return df

def predict_churn(data: dict):
    df = preprocess_input(data)
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]
    return {"churn": int(pred), "churn_probability": float(prob)}
