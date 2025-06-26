# Telco Customer Churn Prediction

This repository contains an end-to-end **MLOps project** built as a final assignment for the [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) organized by **DataTalksClub** (site: https://datatalks.club/) and taught by **Alexey Grigorev**.  

The project focuses on predicting customer churn for a telecom company using ML pipelines, data versioning, experiment tracking, and model deployment via FastAPI.

## Features

- Data ingestion from Kaggle's Telco Customer Churn dataset
- Data preprocessing (type conversion, NA handling, encoding)
- Train-test split and feature engineering
- Model training using Random Forest with MLflow logging
- Model evaluation with accuracy and precision metrics
- Model persistence with joblib
- Testing using pytest
- API deployment using FastAPI
- Experiment tracking using MLflow + DagsHub
- Feature scaling using StandardScaler

## Example FastAPI Usage

### Root Endpoint
``` http
GET /
```
Response
``` json
{ "message": "This is the Telco Customer Churn Prediction API" }
```

### Predict Endpoint
``` http
POST /predict
```
Sample Request
``` json
{
  "gender": "Female",
  "tenure": 12,
  "MonthlyCharges": 80.5,
  "TotalCharges": 956.2
}
```

Response
``` json
{
  "prediction": 1
}

```

## Tech Stack

- Python 3.10
- pandas, scikit-learn, joblib
- MLflow, DagsHub
- FastAPI
- KaggleHub (for dataset ingestion)
- pytest (for testing)

## MLflow Experiment Tracking

- Tracking URI: DagsHub MLflow Dashboard (https://dagshub.com/razamehar/telco-customer-churn-prediction.mlflow)
- Logged artifacts:
- Parameters: max_depth
- Metrics: accuracy, precision
- Artifacts: trained model (.pkl), scaler (.pkl)

## Run Locally
1. Clone the repository
```bash
git clone https://github.com/razamehar/telco-customer-churn-prediction.git
cd telco-customer-churn-prediction
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Start FastAPI app
```bash
uvicorn app.main:app --reload

```

## Run Tests
```bash
pytest tests/
```

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com](mailto:raza.mehar@gmail.com).