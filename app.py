"""FastAPI app for predicting customer churn using a trained ML model."""

import joblib
import numpy as np
from fastapi import FastAPI
from schema import ChurnValues


app = FastAPI()

scaler = joblib.load("scaling/standard_scaler.pkl")
rf_model = joblib.load("./models/rf_model.pkl")

@app.get("/")
def read_root():
    '''
    Root page
    :return: a dictionary message
    '''
    return {"message": "This is the Telco Customer Churn Prediction API"}


@app.post("/predict")
def predict(data: ChurnValues):
    '''
    Loads the model and the scaler, preprocesses the values and returns prediction.
    :param data: churn prediction data
    :return: prediction
    '''

    gender_num = 1 if data.gender == "Female" else 0

    input_features = np.array([
        data.tenure,
        data.MonthlyCharges,
        data.TotalCharges,

    ]).reshape(1, -1)

    scaled_features = scaler.transform(input_features)

    total_charges_per_tenure = data.TotalCharges / data.tenure

    final_features = np.concatenate([[gender_num], scaled_features.flatten(),
                                     [total_charges_per_tenure]]).reshape(1, -1)

    prediction = rf_model.predict(final_features)
    proba = rf_model.predict_proba(final_features)
    confidence = float(np.max(proba))

    return {
        "prediction": int(prediction[0]),
        "confidence": confidence
    }
