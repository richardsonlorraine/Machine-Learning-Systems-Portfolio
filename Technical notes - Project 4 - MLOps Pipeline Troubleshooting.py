from azureml.core import Workspace, Experiment
ws = Workspace.from_config()
exp = Experiment(ws, 'churn_prediction_pipeline') # Retrieve the latest run and inspect failures
for run in exp.get_runs():
    if run.get_status() == "Failed":
        print(f"Error in Run {run.id}: {run.get_details()['error']}")
3. Data Integrity: Guardrail Validation Define "Knowledge Representation" for your data to catch corrupted inputs before they reach the model.
import pandas as pd
def validate_pipeline_data(df): # Rule 1: Check for missing identifiers
    if df['customer_id'].isnull().any():
        raise ValueError("Critical Error: Null customer_id detected.") # Rule 2: Validate categorical integrity
    allowed = {"Bronze", "Silver", "Gold"}
    actual = set(df['membership_level'].unique())
    if not actual.issubset(allowed):
        print(f"Warning: Unexpected levels found: {actual - allowed}") # Example usage
data = pd.read_csv("incoming_batch.csv")
validate_pipeline_data(data)

import pandas as pd
def validate_pipeline_data(df): # Rule 1: Check for missing identifiers
    if df['customer_id'].isnull().any():
        raise ValueError("Critical Error: Null customer_id detected.") # Rule 2: Validate categorical integrity
    allowed = {"Bronze", "Silver", "Gold"}
    actual = set(df['membership_level'].unique())
    if not actual.issubset(allowed):
        print(f"Warning: Unexpected levels found: {actual - allowed}") # Example usage
data = pd.read_csv("incoming_batch.csv")
validate_pipeline_data(data)

import logging # Local file logging for observability
logging.basicConfig(filename='pipeline_ops.log', level=logging.INFO)
try:    # Logic for model inference or training
    logging.info("Model evaluation threshold met: 0.85 accuracy.")
except Exception as e:
    logging.error(f"Pipeline crashed at Evaluation: {str(e)}")