import time
import psutil
import numpy as np
import tensorflow as tp
from sklearn.metrics import accuracy_score, precision_score # 1. Setup & Baseline Training
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)), tf.keras.layers.Dense(128, activation='relu'), tf.keras.layers.Dense(10, activation='softmax')])e
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3, verbose=0) # 2. Multidimensional Evaluation
def run_audit(model, data, labels):    # Metric: Quality & Accuracy
    y_pred = np.argmax(model.predict(data, verbose=0), axis=1)
    acc = accuracy_score(labels, y_pred)    # Metric: Performance (Latency)
    start = time.time()
    for _ in range(50): model.predict(data[:1], verbose=0)
    avg_latency = (time.time() - start) / 50    # Metric: Resource Utilization
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    print(f"Accuracy: {acc:.4f} | Avg Latency: {avg_latency:.4f}s")
    print(f"CPU: {cpu}% | Memory: {mem}%") # 3. Stress Testing (Simulating 10x Load)
print("--- Standard Audit ---")
run_audit(model, x_test, y_test)
print("\n--- Stress Test (High Volume) ---")
large_input = np.repeat(x_test, 10, axis=0) # 100,000 samples
start_stress = time.time()
model.predict(large_input, verbose=0)
print(f"Stress Response Time: {time.time() - start_stress:.2f}s")