import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore
from sklearn.tree import DecisionTreeClassifier # 1. Synthetic System Monitoring Data
np.random.seed(42)
data = {'cpu_usage': np.random.normal(50, 10, 1000), 'network_latency': np.random.normal(100, 20, 1000), 'error_rate': np.random.choice([0, 1], 1000, p=[0.95, 0.05])}
df = pd.DataFrame(data) # 2. Issue Detection (Unsupervised)
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(df) # 3. Anomaly Attribution (Why did it fail?)
z_scores = df[['cpu_usage', 'network_latency']].apply(zscore)
def get_cause(row):
    if row['anomaly'] == 1: return "Normal"    # Identify which metric exceeded 3 standard deviations
    failed_cols = [col for col in z_scores.columns if abs(z_scores.loc[row.name, col]) > 3]
    return failed_cols if failed_cols else "General Logic Error" # 4. Actionable Recommendations
def recommend_fix(cause):
    solutions = {"network_latency": "Restart network service / Flush DNS.", "cpu_usage": "Scale compute instance or kill rogue processes."}
    return solutions.get(cause[0] if isinstance(cause, list) else cause, "Escalate to Human.") # 5. Testing with a Simulated Network Spike
df.at[0, 'network_latency'] = 1000 
cause = get_cause(df.iloc[0])
print(f"Detected Cause: {cause}")
print(f"Action: {recommend_fix(cause)}")