# Logic for an Automated Monitoring Alert
def monitor_model_health(current_metrics, threshold_metrics):
    # Detect Performance Decay (Drift)
    if current_metrics['accuracy'] < threshold_metrics['min_accuracy']:
        trigger_alert("Model Drift Detected")
        trigger_retrain_pipeline(dataset="latest_prod_data")
        return "Action: Retraining Initiated"
    return "Status: Healthy"