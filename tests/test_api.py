from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_predict_endpoint_ok():
    payload = {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 10,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.35,
        "TotalCharges": 1397.0
    }
    resp = client.post("/predict", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert "churn_probability" in body and "prediction" in body
    assert 0.0 <= body["churn_probability"] <= 1.0
    assert body["prediction"] in (0, 1)
