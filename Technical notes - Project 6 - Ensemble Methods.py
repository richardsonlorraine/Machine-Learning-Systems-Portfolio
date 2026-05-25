import numpy as np # Mock Data: Features and Errors
data_points = np.array([1, 2, 3, 4, 5])
errors = np.array([0.1, 0.5, 0.05, 0.8, 0.1]) # High error on point 4  # --- BAGGING LOGIC (Parallel/Independent) ---
def bagging_step(data):    # Randomly sample with replacement
    subset = np.random.choice(data, size=len(data), replace=True)
    return f"Model trained on subset: {subset}" # --- BOOSTING LOGIC (Sequential/Corrective) ---
def boosting_step(data, current_errors):    # Identify "hard" cases (index 3 is high error)
    weights = current_errors / np.sum(current_errors)
    return f"New model focused on points with weights: {weights.round(2)}"
print("Bagging:", bagging_step(data_points))
print("Boosting:", boosting_step(data_points, errors))