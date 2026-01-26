from pydantic import BaseModel

class ChurnRequest(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    PaymentMethod: str
    OnlineSecurity: str
    TechSupport: str
    InternetService: str
    OnlineBackup: str
    PaperlessBilling: str
    MultipleLines: str
    gender: str
    DeviceProtection: str
    Partner: str
    Dependents: str
    StreamingMovies: str
    StreamingTV: str
