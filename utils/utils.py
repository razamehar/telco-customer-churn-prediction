import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os


def save_data(df, filename, folder):
    os.makedirs(f"./data/{folder}", exist_ok=True)
    path = os.path.join(f"./data/{folder}", filename)
    df.to_csv(path, index=False)
    print(f"Saved data to {path}")


def standardize_data(train_df, test_df):
    cols_to_scale = ['tenure', 'MonthlyCharges', 'TotalCharges']

    for col in cols_to_scale:
        train_df[col] = pd.to_numeric(train_df[col], errors='coerce')
        test_df[col] = pd.to_numeric(test_df[col], errors='coerce')

    train_df.dropna(subset=cols_to_scale, inplace=True)
    test_df.dropna(subset=cols_to_scale, inplace=True)

    scaler = StandardScaler()

    train_scaled = scaler.fit_transform(train_df[cols_to_scale])
    test_scaled = scaler.transform(test_df[cols_to_scale])

    os.makedirs("./scaling", exist_ok=True)
    joblib.dump(scaler, "./scaling/standard_scaler.pkl")
    print("scaler pipeline saved")

    train_df[cols_to_scale] = pd.DataFrame(train_scaled, columns=cols_to_scale, index=train_df.index)
    test_df[cols_to_scale] = pd.DataFrame(test_scaled, columns=cols_to_scale, index=test_df.index)

    print("Data scaled")
    return train_df, test_df
