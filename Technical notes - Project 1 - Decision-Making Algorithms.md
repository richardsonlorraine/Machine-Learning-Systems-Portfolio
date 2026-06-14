Decision-Making Algorithms

Decision-making algorithms are the "operational core" of AI, enabling systems to process data and recommend outcomes. They are categorized by the nature of the environment they navigate: Certain (predictable outcomes) or Uncertain (probabilistic outcomes).

1. Environments and Frameworks

Environment Type -> Key Characteristics -> Common Algorithms

Certain -> Known outcomes; pathfinding focus. -> BFS, DFS, A* Search

Uncertain -> Risk and incomplete info; probabilistic. -> MDPs, Bayesian Networks, Reinforcement Learning

* Markov Decision Processes (MDPs): A mathematical framework for modeling decision-making where outcomes are partly random and partly controlled by the agent.
* Reinforcement Learning (RL): An agent learns optimal policies via trial-and-error, receiving rewards or penalties to maximize cumulative gain.

2. Machine Learning Algorithms for Decisions

* Decision Trees: Flowchart-like structures splitting data based on feature thresholds. They are highly interpretable but prone to overfitting.
* Random Forests: An ensemble method that averages multiple decision trees to increase stability and accuracy.
* Support Vector Machines (SVM): Finds the optimal hyperplane to separate classes with the maximum margin in high-dimensional spaces.
* Bayesian Networks: Probabilistic graphical models representing variables and their conditional dependencies.
* Genetic Algorithms: Optimization techniques inspired by natural selection (mutation, crossover, and fitness functions).

3. Implementation: Decision Tree Logic

This implementation uses the Scikit-Learn library to build a model that predicts medical outcomes (Breast Cancer dataset) using an explainable decision-making logic.

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

4. Recommendation Engine (KNN Approach)

For scenarios where a system must recommend a solution based on similar past problems, K-Nearest Neighbors (KNN) is often used.

* Logic: Finds the "K" closest examples in the feature space to provide a recommendation.
* Hyperparameter Tuning: Adjusting n_neighbors (e.g., changing from 5 to 7) is crucial to improving accuracy.

from sklearn.neighbors import KNeighborsClassifier # Initialize KNN with 5 neighbors

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)

print(f"KNN Accuracy: {accuracy_score(y_test, y_pred_knn) * 100:.2f}%")

5. Summary Checklist for Implementation

* Data Integrity: Use median imputation for missing values.
* Validation: Always use a stratified train-test split to ensure the model generalizes.
* Explainability: Use visualization tools (like plot_tree) to ensure decisions are transparent and ethical.
Optimization: Systematically tune parameters using Grid Search to find the global optima.
