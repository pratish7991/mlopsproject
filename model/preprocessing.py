import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocess(df: pd.DataFrame, encoder=None, scaler=None, fit: bool = False):
    df = df.copy()

    # Separate target if exists
    y = df.pop('churned') if 'churned' in df.columns else None

    # Encode contract_type
    contract_type = df[['contract_type']]
    if fit:
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded = encoder.fit_transform(contract_type)
    else:
        encoded = encoder.transform(contract_type)

    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['contract_type']))
    df = df.drop(columns=['contract_type']).reset_index(drop=True)
    df = pd.concat([df, encoded_df], axis=1)

    # Drop customer_id and scale
    if 'customer_id' in df.columns:
        df = df.drop(columns=['customer_id'])

    if fit:
        scaler = StandardScaler()
        scaled = scaler.fit_transform(df)
    else:
        scaled = scaler.transform(df)

    return scaled, y.values if y is not None else None, encoder, scaler, df.columns.tolist()
