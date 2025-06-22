import pandas as pd
from sklearn.model_selection import train_test_split
from utils.utils import save_data
from src.data_ingestion import data_ingestion
from src.data_preprocessing import preprocess_data
from utils.utils import standardize_data


def main():
    try:
        df = data_ingestion("blastchar/telco-customer-churn")
        preprocessed_df = preprocess_data(df)
        train_data, test_data = train_test_split(preprocessed_df, test_size=0.2, random_state=42)
        train_scaled_df, test_scaled_df = standardize_data(train_data, test_data)
        save_data(train_scaled_df, "preprocessed_train.csv")
        save_data(test_scaled_df, "preprocessed_test.csv")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to complete the data ingestion process.")

if __name__ == '__main__':
    main()