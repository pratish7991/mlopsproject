import joblib
import pandas as pd

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model", "model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "model", "encoder.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "model", "scaler.pkl"))
feature_names = joblib.load(os.path.join(BASE_DIR, "model", "feature_names.pkl"))


def predict_churn(data: dict):
    df = pd.DataFrame([data])

    # Encode
    contract_encoded = encoder.transform(df[['contract_type']])
    encoded_df = pd.DataFrame(contract_encoded, columns=encoder.get_feature_names_out(['contract_type']))

    df = df.drop(columns=['contract_type', 'customer_id'], errors='ignore')
    df = pd.concat([df.reset_index(drop=True), encoded_df], axis=1)

    # Ensure column order consistency
    df = df.reindex(columns=feature_names, fill_value=0)

    # Scale
    df_scaled = scaler.transform(df)

    # Predict
    pred = model.predict(df_scaled)[0]
    prob = model.predict_proba(df_scaled)[0][1]  # Probability of class '1'

    return {"prediction": int(pred), "probability": round(float(prob), 4)}

