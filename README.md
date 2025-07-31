## Churn Prediction MLOps Project

This project trains a churn model, logs to MLflow, and serves it via FastAPI.

### To run locally:
```bash
pip install -r requirements.txt
python model/train.py
uvicorn api.main:app --reload
