from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt # 1. Load Data
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target # 2. Preprocess & Split (Handling missing values with median)
df.fillna(df.median(), inplace=True)
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 3. Implement Decision Tree (Max depth prevents overfitting)
tree = DecisionTreeClassifier(max_depth=4)
tree.fit(X_train, y_train) # 4. Predict & Evaluate
y_pred = tree.predict(X_test)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%") # 5. Visualize Logic
plt.figure(figsize=(12,8))
plot_tree(tree, filled=True, feature_names=X.columns, class_names=['Malignant', 'Benign'])
plt.show()

from sklearn.neighbors import KNeighborsClassifier # Initialize KNN with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print(f"KNN Accuracy: {accuracy_score(y_test, y_pred_knn) * 100:.2f}%")