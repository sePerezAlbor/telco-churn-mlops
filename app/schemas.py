from pydantic import BaseModel


class CustomerData(BaseModel):
    gender: str             # ['Female' 'Male']
    SeniorCitizen: int
    Partner: str            # ['Yes' 'No']
    Dependents: str         # ['Yes' 'No']
    tenure: int
    PhoneService: str       # ['Yes' 'No']
    MultipleLines: str      # ['Yes' 'No']
    InternetService: str    # ['DSL' 'Fiber optic' 'No']
    OnlineSecurity: str     # ['Yes' 'No']
    OnlineBackup: str       # ['Yes' 'No']
    DeviceProtection: str   # ['Yes' 'No']
    TechSupport: str        # ['Yes' 'No']
    StreamingTV: str        # ['Yes' 'No']     
    StreamingMovies: str    # ['Yes' 'No']
    Contract: str           # ['Month-to-month' 'One year' 'Two year']
    PaperlessBilling: str   # ['Yes' 'No']
    PaymentMethod: str      # ['Electronic check' 'Mailed check' 'Bank transfer (automatic)' 'Credit card (automatic)']
    MonthlyCharges: float
    TotalCharges: float
