import pandas as pd
import logging

logging.basicConfig(filename='pipeline_ops.log', level=logging.INFO)

def validate_pipeline_data(df): 
    if df['customer_id'].isnull().any():
        raise ValueError("Critical Error: Null customer_id detected.") 
    
    allowed = {"Bronze", "Silver", "Gold"}
    actual = set(df['membership_level'].unique())
    if not actual.issubset(allowed):
        print(f"Warning: Unexpected levels found: {actual - allowed}")

# Operational validation check
try:
    # Simulated metrics evaluation evaluation
    current_accuracy = 0.79 
    target_threshold = 0.85
    
    if current_accuracy < target_threshold:
        raise ValueError(f"Performance baseline missed. Expected >={target_threshold}, got {current_accuracy}")
    
    logging.info(f"Model evaluation threshold met: {current_accuracy} accuracy.")
except Exception as e:
    logging.error(f"Pipeline crashed at Evaluation: {str(e)}")
