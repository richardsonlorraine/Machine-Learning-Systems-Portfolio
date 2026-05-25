import pandas as pd
import logging # Configure logging to save to a file for long-term audit
logging.basicConfig(filename='ml_system.log', level=logging.INFO, format='%(levelname)s:%(asctime) s:%(message)s')
def safe_predict(model, input_data):
    """Validates data and handles inference errors gracefully."""
    try: # 1. Input Validation
        if not isinstance(input_data, pd.DataFrame):
            logging.error("Inference failed: Input is not a DataFrame.")
            raise ValueError("User Error: Please provide data in CSV/DataFrame format.")
        if input_data.isnull().values.any():
            logging.warning("Missing values detected. Imputing with 0.")
            input_data = input_data.fillna(0) # 2. Inference Logic
        logging.info("Starting model prediction...")
        predictions = model.predict(input_data)
        logging.info("Prediction successful.")
        return predictions
    except ValueError as ve:        # User-friendly error message
        print(f"Action Required: {ve}")
        return None
    except Exception as e:        # Technical log for developers
        logging.error(f"Unexpected System Error: {e}", exc_info=True)
        return None # Usage example
# results = safe_predict(trained_model, test_df)