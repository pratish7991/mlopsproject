from pydantic import BaseModel

class InferenceRequest(BaseModel):
    customer_id: str
    contract_type: str
    age: int
    monthly_charges: float
    has_internet: int
    tenure_months: int
