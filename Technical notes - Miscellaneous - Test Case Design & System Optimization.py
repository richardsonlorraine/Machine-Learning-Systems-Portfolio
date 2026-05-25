import tensorflow as tf
import tensorflow_model_optimization as tfmot
import numpy as np # 1. Setup: Load and train a baseline model (MNIST)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)), tf.keras.layers.Dense(128, activation='relu'), tf.keras.layers.Dense(10, activation='softmax')])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=1) # 2. Model Pruning: Remove neurons with low contribution
pruning_params = {'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(initial_sparsity=0.0, final_sparsity=0.50, begin_step=0, end_step=1000)}
pruned_model = tfmot.sparsity.keras.prune_low_magnitude(model, pruning_params)
pruned_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# Update internal pruning steps during training
callbacks = [tfmot.sparsity.keras.UpdatePruningStep()]
pruned_model.fit(x_train, y_train, epochs=1, callbacks=callbacks) # 3. Model Quantization: Convert from 32-bit float to 8-bit integer
# Strip pruning wrappers before conversion
final_model = tfmot.sparsity.keras.strip_pruning(pruned_model)
converter = tf.lite.TFLiteConverter.from_keras_model(final_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_tflite_model = converter.convert()
print("Optimization Complete: Model is now pruned (50% sparse) and quantized (8-bit).")