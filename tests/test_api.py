from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", data={
        "customer_id": "123",
        "contract_type": "Month-to-month",
        "age": 45,
        "monthly_charges": 90.5,
        "has_internet": 1,
        "tenure_months": 12
    })
    assert response.status_code == 200
    assert "Prediction:" in response.text
