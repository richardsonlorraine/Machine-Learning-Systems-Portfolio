import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2  # 1. Load Pre-trained Base (ImageNet knowledge) # include_top=False removes the original 1000-class classifier
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(32, 32, 3)) # 2. Freeze the base knowledge
base_model.trainable = False # 3. Add a custom 'Head' for our 10-class problem
model = models.Sequential([base_model, layers.GlobalAveragePooling2D(), layers.Dense(128, activation='relu'), layers.Dropout(0.2), layers.Dense(10, activation='softmax')])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # history = model.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val))
Module 2: The Baseline (From Scratch)
baseline_model = models.Sequential([layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)), layers.MaxPooling2D((2, 2)), layers.Flatten(), layers.Dense(64, activation='relu'), layers.Dense(10, activation='softmax')]) # This model starts with zero knowledge and takes longer to converge.

# Create a model that stops at a specific convolutional block
visualization_model = models.Model(inputs=model.input, outputs=base_model.get_layer ('block_1_expand_relu').output) # Predict on one image to see the 'filtered' version
feature_maps = visualization_model.predict(x_test[:1]) # Output: A set of images showing emphasized edges or specific textures.