import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    data = {
        'gender': ['Male', 'Female', 'Female', 'Male', 'Male'],
        'tenure': [1, 2, 3, 4, 5],
        'MonthlyCharges': ['70.35', '80.5', 'not_a_number', '90.1', '70.35'],
        'TotalCharges': ['100.5', '200.7', '300.8', None, '100.5'],
        'Churn': ['No', 'Yes', 'No', 'Yes', 'No'],
        'ExtraColumn': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)

    processed_df = preprocess_data(df)

    expected_columns = ['gender', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']
    assert list(processed_df.columns) == expected_columns
    assert processed_df.isna().sum().sum() == 0
    assert processed_df['gender'].isin([0,1]).all()
    assert processed_df['Churn'].isin([0,1]).all()
    assert pd.api.types.is_numeric_dtype(processed_df['MonthlyCharges'])
    assert pd.api.types.is_numeric_dtype(processed_df['TotalCharges'])
    assert len(processed_df) == len(processed_df.drop_duplicates())
    assert len(processed_df) == 3
