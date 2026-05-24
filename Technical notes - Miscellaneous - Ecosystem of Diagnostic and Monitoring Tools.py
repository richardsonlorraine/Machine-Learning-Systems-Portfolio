import pandas as pd
def check_data_quality(df):    # Check for missing values
    if df['customer_id'].isnull().any():    
        print("🚨 Alert: Missing customer IDs detected!")    # Check for valid categorical values (Data Integrity)        
    valid_levels = {"Bronze", "Silver", "Gold"}  
    current_levels = set(df['membership_level'].unique())    
    if not current_levels.issubset(valid_levels):    
        invalid = current_levels - valid_levels        
        print(f"❌ Validation Error: Invalid levels found: {invalid}")        
    else:    
        print("✅ Data Quality Check Passed.") # Example Usage       
incoming_df = pd.read_csv("new_users.csv")
check_data_quality(incoming_df)
from azureml.core import Workspace
def enable_monitoring(service_name):
    ws = Workspace.from_config()   
    service = ws.webservices[service_name]    # Enable Proactive Alerting
    if not service.app_insights_enabled:    
        service.update(enable_app_insights=True)        
        print(f"Monitoring active for {service_name}")    # URL for the Real-time Dashboard        
    print(f"View metrics at: {service.scoring_uri}")