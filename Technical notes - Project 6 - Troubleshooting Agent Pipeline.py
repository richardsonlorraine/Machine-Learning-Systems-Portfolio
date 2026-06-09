import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore # 1. Synthetic Data Generation (The "Sensor" data)
np.random.seed(42)
n_samples = 1000
data = {'cpu_usage': np.random.normal(50, 10, n_samples), 'memory_usage': np.random.normal(60, 15, n_samples), 'network_latency': np.random.normal(100, 20, n_samples), 'error_rate': np.random.choice([0, 1], n_samples, p=[0.95, 0.05])}
df = pd.DataFrame(data) # 2. Issue Detection (Isolation Forest)
def detect_anomalies(data): # 'contamination' defines the expected % of outliers
model = IsolationForest(contamination=0.05, random_state=42)
return model.fit_predict(data)
df['anomaly'] = detect_anomalies(df.select_dtypes(include=[np.number])) # 3. Statistical Deep Dive (Explainability via Z-Scores)
z_scores = df.select_dtypes(include=[np.number]).apply(zscore)
def find_root_cause_columns(row, threshold=3):
if row['anomaly'] == 1: return [] # Normal data    # Find columns where the value is > 3 standard deviations from the mean
return [col for col in z_scores.columns if abs(z_scores.loc[row.name, col]) > threshold]
df['root_cause'] = df.apply(find_root_cause_columns, axis=1) # 4. Prescription Logic (Solution Recommendation)
def recommend_solution(causes):
mapping = {"network_latency": "Restart network service or check gateway.", "cpu_usage": "Identify and kill rogue processes.", "memory_usage": "Flush cache or increase swap space."}
return [mapping.get(c, "Escalate to Level 2 Support.") for c in causes] # 5. Testing the Agent