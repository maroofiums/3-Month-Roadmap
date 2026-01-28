import joblib

model = joblib.load("model.pkl")

def predict_iris(features):
    prediction = model.predict([features])
    return int(prediction[0])
