import pandas as pd
import kagglehub
import shutil
import os
from sklearn.model_selection import train_test_split
from utils.utils import *
from src.data_preprocessing import preprocess_data
import warnings
warnings.filterwarnings('ignore')


def data_ingestion(link):
    path = kagglehub.dataset_download(link)
    print("Data downloaded from Kaggle")

    custom_path = "./data"
    os.makedirs(custom_path, exist_ok=True)

    for filename in os.listdir(path):
        shutil.copy(os.path.join(path, filename), os.path.join(custom_path, filename))

    print("Data copied to:", custom_path)

    loaded_df = pd.read_csv("./data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    print("Data loaded in the data frame")

    return loaded_df


def main():
    print("Ingestion started...")
    try:
        os.makedirs("./data", exist_ok=True)

        os.makedirs("./data/ingested", exist_ok=True)

        df = data_ingestion("blastchar/telco-customer-churn")
        preprocessed_df = preprocess_data(df)
        train_data, test_data = train_test_split(preprocessed_df, test_size=0.2, random_state=42)
        train_scaled_df, test_scaled_df = standardize_data(train_data, test_data)
        save_data(train_scaled_df, "preprocessed_train.csv", "ingested")
        save_data(test_scaled_df, "preprocessed_test.csv", "ingested")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to complete the data ingestion process.")

if __name__ == '__main__':
    main()