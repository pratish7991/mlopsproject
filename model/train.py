import pandas as pd
import mlflow
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from preprocessing import preprocess

df = pd.read_csv("data/dummy_customer_churn.csv")

X, y, encoder, scaler, feature_names = preprocess(df, fit=True)

model = LogisticRegression()
model.fit(X, y)

# Log to MLflow
with mlflow.start_run():
    acc = accuracy_score(y, model.predict(X))
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

# Save model and transformers
joblib.dump(model, "model/model.pkl")
joblib.dump(encoder, "model/encoder.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(feature_names, "model/feature_names.pkl")
