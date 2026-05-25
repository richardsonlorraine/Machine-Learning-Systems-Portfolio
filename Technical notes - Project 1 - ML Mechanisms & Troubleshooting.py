import pandas as pd
import logging
from sklearn.tree import DecisionTreeClassifier # 1. Environment Setup & Logging Configuration
logging.basicConfig(filename='ml_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
def validate_and_train(data, target_col):
    try:        # 2. Input Validation (Issue Identification)
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        if data.isnull().values.any():   # Autonomous Fix: Attempting to handle missing data via median
            logging.warning("Missing values detected. Applying median imputation.")
            data = data.fillna(data.median())        # 3. Model Training (Logic Mechanism)
        X = data.drop(target_col, axis=1)
        y = data[target_col]
        model = DecisionTreeClassifier()
        model.fit(X, y)
        print("Mechanism Executed: Model trained successfully.")
        return model
    except Exception as e:        # 4. Root Cause Logging
        logging.error(f"Pipeline Failure: {e}")
        print(f"Troubleshooting Alert: {e}")
        return None # 5. Stress Testing (Test-Driven Development)
# Intentionally introducing a 'None' value to verify the troubleshooting path
df_faulty = pd.DataFrame({'feature1': [1, 2, None], 'target': [0, 1, 0]})
validate_and_train(df_faulty, 'target')