import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score
import joblib
import os
import mlflow
from mlflow.models.signature import infer_signature
import dagshub


dagshub.init(repo_owner='razamehar', repo_name='telco-customer-churn-prediction', mlflow=True)
remote_server_uri = "https://dagshub.com/razamehar/telco-customer-churn-prediction.mlflow"
mlflow.set_tracking_uri(remote_server_uri)


def eval_metrics(actual, pred):
    accuracy = accuracy_score(actual, pred)
    precision = precision_score(actual, pred)
    return accuracy, precision


os.makedirs('./models', exist_ok=True)
os.makedirs('./data/evaluation', exist_ok=True)

train_df = pd.read_csv('./data/featurized/final_train.csv')
y_train = train_df['Churn']
X_train = train_df.drop('Churn', axis=1)

max_depth = None

with mlflow.start_run():
    # Train model
    rf_model = RandomForestClassifier(max_depth=max_depth)
    rf_model.fit(X_train, y_train)


    joblib.dump(rf_model, "./models/rf_model.pkl")

    test_df = pd.read_csv('./data/featurized/final_test.csv')
    y_test = test_df['Churn']
    X_test = test_df.drop('Churn', axis=1)


    y_pred = rf_model.predict(X_test)
    accuracy, precision = eval_metrics(y_test, y_pred)

    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)

    mlflow.log_artifact("./models/rf_model.pkl", artifact_path="model")

    signature = infer_signature(X_train, rf_model.predict(X_train))
    mlflow.set_tag("signature", str(signature))
    mlflow.set_tag("input_example", str(X_train.iloc[:5].to_dict()))