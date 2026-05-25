import logging
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # 1. Initialize the Audit Trail
logging.basicConfig(filename='ml_pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Pipeline Initialized.")
def run_traceable_pipeline(data_path):
    try:  # 2. Data Ingestion & Preprocessing Logs
        logging.info(f"Loading data from {data_path}")
        df = pd.read_csv(data_path) # Log data integrity actions
        df.fillna(0, inplace=True)
        logging.info("Missing values handled (Imputation: 0).")   # 3. Model Training & Validation Logs
        X, y = df.iloc[:, :-1], df.iloc[:, -1]
        model = DecisionTreeClassifier()
        logging.info("Starting model training...")
        model.fit(X, y)
        acc = model.score(X, y)
        logging.info(f"Training complete. Accuracy: {acc:.2f}") # 4. Inference Audit
        predictions = model.predict(X[:5])
        logging.info(f"Inference sample: {predictions}")
    except Exception as e:  # Root Cause Analysis
        logging.error(f"PIPELINE FAILURE: {str(e)}") # Example call (assumes your-dataset.csv exists)
run_traceable_pipeline('your-dataset.csv')
