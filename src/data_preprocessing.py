import pandas as pd


def preprocess_data(df):
    cols_to_keep = ['gender', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']
    preprocessed_df = df[cols_to_keep].copy()

    preprocessed_df['TotalCharges'] = pd.to_numeric(preprocessed_df['TotalCharges'], errors='coerce')
    preprocessed_df['MonthlyCharges'] = pd.to_numeric(preprocessed_df['MonthlyCharges'], errors='coerce')
    preprocessed_df.dropna(inplace=True)
    preprocessed_df = preprocessed_df.drop_duplicates()

    preprocessed_df['gender'] = preprocessed_df['gender'].map({'Male': 0, 'Female': 1})
    preprocessed_df['Churn'] = preprocessed_df['Churn'].map({'No': 0, 'Yes': 1})

    print("Data preprocessed")
    return preprocessed_df