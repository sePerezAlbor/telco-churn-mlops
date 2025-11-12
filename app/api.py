from fastapi import FastAPI
from .schemas import CustomerData
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("app/model.joblib")


@app.post("/predict")
def predict(data: CustomerData):
    df = pd.DataFrame([data.model_dump()])
    p = model.predict_proba(df)[0][1]
    return {"churn_probability": float(p), "prediction": int(p > 0.5)}
