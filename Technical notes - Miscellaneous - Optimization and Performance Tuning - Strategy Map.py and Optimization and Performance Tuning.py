def representative_data_gen():
    # Pass a small slice (e.g., 100 samples) of calibration data to register the activation scales
    for input_value in tf.data.Dataset.from_tensor_slices(X_train_samples).batch(1).take(100):
        yield [tf.cast(input_value, tf.float32)]

converter = tf.lite.TFLiteConverter.from_keras_model(final_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# Fix: Anchor the optimization scaling with structural data ranges
converter.representative_dataset = representative_data_gen
