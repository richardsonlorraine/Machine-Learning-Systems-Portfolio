import tensorflow as tf
import tensorflow_model_optimization as tfmot
import numpy as np # 1. Pruning: Trimming the "Fat"
pruning_params = {'pruning_schedule': 
tfmot.sparsity.keras.PolynomialDecay(initial_sparsity=0.0, final_sparsity=0.5, begin_step=0, end_step=1000)} # Apply pruning to a pre-trained model
pruned_model = tfmot.sparsity.keras.prune_low_magnitude(base_model, pruning_params)
pruned_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy') # Strip wrappers for deployment
final_model = tfmot.sparsity.keras.strip_pruning(pruned_model) # 2. Quantization: Reducing Precision for Speed
converter = tf.lite.TFLiteConverter.from_keras_model(final_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_tflite_model = converter.convert() # Result: A model ~4x smaller and significantly faster on edge devices.