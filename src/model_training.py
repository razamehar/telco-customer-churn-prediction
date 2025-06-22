import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os


os.makedirs('./models', exist_ok=True)

train_df = pd.read_csv('./data/featurized/final_train.csv')

y_train = train_df['Churn']
X_train = train_df.drop('Churn', axis=1)

rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
print("Random Forest Regressor trained")

joblib.dump(rf_model, "./models/rf_model.pkl")
print("Trained model saved")