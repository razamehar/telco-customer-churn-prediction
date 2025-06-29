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
- Testing using `pytest`
- Code linting using `pylint`
- API deployment using FastAPI
- Experiment tracking using MLflow + DagsHub
- Feature scaling using StandardScaler
- Data versioning using DVC
- Docker containerization for consistent reproducibility
- CI/CD pipeline using GitHub Actions
- Model artifacts pulled from GitHub Releases during build

## FastAPI Usage - Example

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

- **Python 3.10**
- **Data & Modeling**: pandas, scikit-learn, joblib
- **Experiment Tracking**: MLflow, DagsHub
- **API & Deployment**: FastAPI
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Data Ingestion**: Kaggle (via kaggle CLI or KaggleHub)
- **Version Control**: DVC (Data Version Control)
- **Testing & Code Quality**: pytest, pylint

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

## Docker Support
### Build Docker Image
```bash
docker build -t churn-predictor .
```

### Run Docker Container
```bash
docker run -d -p 8000:8000 churn-predictor
``` 

## Run Tests
```bash
pytest tests/
```

## Run Linting
```bash
pylint app/*.py
```

## CI/CD with GitHub Actions
This project includes a CI/CD pipeline using GitHub Actions that:

- Installs dependencies
- Runs tests with pytest
- Lints code using pylint
- Builds the Docker image
- Ensures model and scaler are downloaded from GitHub Releases
- CI config: .github/workflows/main.yml

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com](mailto:raza.mehar@gmail.com).