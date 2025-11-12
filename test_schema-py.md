# Running the FastAPI Application

To run the FastAPI application, use the following command in your terminal (with the environment activated if you are using a virtual environment):

```bash
uvicorn app.api:app --reload
```

Then open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) and test the endpoints /predict, paste the example JSON payload:

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 8,
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
}
```

to see the prediction results.
