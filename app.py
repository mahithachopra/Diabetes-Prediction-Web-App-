# app.py (FastAPI Version)
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

class InputData(BaseModel):
    features: list

@app.post('/predict')
def predict(data: InputData):
    X = np.array([data.features])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]
    return {"prediction": int(prediction)}
