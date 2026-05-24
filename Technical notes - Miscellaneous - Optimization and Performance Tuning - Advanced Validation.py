from sklearn.model_selection import cross_val_score
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
# Wrapping Keras for Scikit-Learn compatibility
def create_model(): # ... model architecture ...
    return model
keras_model = KerasClassifier(build_fn=create_model, epochs=5, batch_size=32, verbose=0)
cv_scores = cross_val_score(keras_model, x_train, y_train, cv=5)
print(f"Mean Stability: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")