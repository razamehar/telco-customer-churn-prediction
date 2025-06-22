import joblib
from sklearn.metrics import mean_absolute_error, r2_score
import json
import pandas as pd


test_df = pd.read_csv('./data/final_test.csv')

y_test = test_df['Churn']
X_test = test_df.drop('Churn', axis=1)

rf_model = joblib.load("./models/rf_model.pkl")
print("Model loaded")

y_pred = rf_model.predict(X_test)
print("Prediction made by the model")

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.4f}")
print(f"R² Score: {r2:.4f}")

metrics_dict={
    'mae':mae,
    'r2':r2
}

with open('./models/metrics.json', 'w') as f:
    json.dump(metrics_dict, f)
print("Metrics saved to ../models/metrics.json")