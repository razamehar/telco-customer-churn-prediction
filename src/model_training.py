import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
import joblib


train_df = pd.read_csv('./data/final_train.csv')

y_train = train_df['Churn']
X_train = train_df.drop('Churn', axis=1)

rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
print("Random Forest Regressor trained")

joblib.dump(rf_model, "./models/rf_model.pkl")
print("Trained model saved")