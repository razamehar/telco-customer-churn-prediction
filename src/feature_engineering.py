import pandas as pd
from utils.utils import save_data
import os


os.makedirs("./data/featurized", exist_ok=True)

train_df = pd.read_csv("./data/ingested/preprocessed_train.csv")
test_df = pd.read_csv("./data/ingested/preprocessed_test.csv")

train_df["total_charges_per_tenure"] = train_df["TotalCharges"] / train_df["tenure"]
test_df["total_charges_per_tenure"] = test_df["TotalCharges"] / test_df["tenure"]

save_data(train_df, "final_train.csv", "featurized")
save_data(test_df, "final_test.csv", "featurized")