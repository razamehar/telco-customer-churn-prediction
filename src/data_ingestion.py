import pandas as pd
import kagglehub
import shutil
import os
import warnings
warnings.filterwarnings('ignore')


def data_ingestion(link):
    path = kagglehub.dataset_download(link)
    print("Data downloaded from Kaggle")

    custom_path = "../data"
    os.makedirs(custom_path, exist_ok=True)

    for filename in os.listdir(path):
        shutil.copy(os.path.join(path, filename), os.path.join(custom_path, filename))

    print("Data copied to:", custom_path)

    loaded_df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    print("Data loaded in the data frame")

    return loaded_df