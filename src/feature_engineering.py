import pandas as pd
from utils.utils import save_data


train_df = pd.read_csv("./data/preprocessed_train.csv")
test_df = pd.read_csv("./data/preprocessed_test.csv")

train_df["total_charges_per_tenure"] = train_df["TotalCharges"] / train_df["tenure"]
test_df["total_charges_per_tenure"] = test_df["TotalCharges"] / test_df["tenure"]

save_data(train_df, "final_train.csv")
save_data(test_df, "final_test.csv")