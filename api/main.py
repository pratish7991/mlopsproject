from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.predict import predict_churn
import os

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "..", "templates"))

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request,
            customer_id: str = Form(...),
            contract_type: str = Form(...),
            age: int = Form(...),
            monthly_charges: float = Form(...),
            has_internet: int = Form(...),
            tenure_months: int = Form(...)):

    input_data = {
        "customer_id": customer_id,
        "contract_type": contract_type,
        "age": age,
        "monthly_charges": monthly_charges,
        "has_internet": has_internet,
        "tenure_months": tenure_months
    }

    result = predict_churn(input_data)
    return templates.TemplateResponse("form.html", {"request": request, "result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
