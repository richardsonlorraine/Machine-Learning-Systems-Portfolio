import numpy as np
def get_private_mean(data, epsilon):
    """Calculates a differentially private mean. Sensitivity for a mean of values in range [0, 1] is 1/N. """
    actual_mean = np.mean(data)    
    n = len(data)    # Sensitivity of the mean query   
    sensitivity = 1.0 / n    # Laplace Mechanism: Noise = Scale * Laplace(0, 1)    
    # Scale = Sensitivity / Epsilon    
    scale = sensitivity / epsilon    
    noise = np.random.laplace(0, scale)    
    return actual_mean + noise # 1. Sample Dataset (e.g., User ratings from 0 to 1)    
user_data = np.random.random(1000) # 2. Privacy Budget (Lower epsilon = More privacy, more noise)
epsilon_strict = 0.1
epsilon_loose = 1.0
print(f"Actual Mean: {np.mean(user_data):.5f}")
print(f"Private Mean (strict, ε=0.1): {get_private_mean(user_data, epsilon_strict):.5f}")
print(f"Private Mean (loose, ε=1.0): {get_private_mean(user_data, epsilon_loose):.5f}")