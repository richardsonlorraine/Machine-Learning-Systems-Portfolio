import numpy as np
# Mock local weight updates from 3 hospitals (clients)
client_updates = [np.array([0.15, 0.22, 0.08]), # Hospital A
    np.array([0.12, 0.25, 0.10]), # Hospital B
    np.array([0.18, 0.20, 0.05])  # Hospital C]
def federated_averaging(updates):    # The server only sees these numbers, not the patients' files
    global_weights = np.mean(updates, axis=0)
    return global_weights
new_global_model = federated_averaging(client_updates)
print(f"Updated Global Model: {new_global_model}")