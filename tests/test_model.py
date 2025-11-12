import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "app", "model.joblib")

def test_model_file_exists():
    assert os.path.exists(MODEL_PATH), "app/model.joblib no existe"

def test_model_can_predict_proba():
    model = joblib.load(MODEL_PATH)
    # usa las mismas columnas de entrenamiento (strings crudos)
    row = pd.DataFrame([{
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 89.5,
        "TotalCharges": 420.0
    }])
    proba = model.predict_proba(row)
    assert proba.shape == (1, 2)
    assert 0.0 <= float(proba[0, 1]) <= 1.0
