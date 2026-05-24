import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt # 1. Data Structuring
data = {'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'PrevExamScore': [30, 40, 45, 50, 60, 65, 70, 75, 80, 85], 'Pass': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]}
df = pd.DataFrame(data)
X, y = df[['StudyHours', 'PrevExamScore']], df['Pass']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 2. Logistic Regression (The "Simple" Linear Model)
log_model = LogisticRegression().fit(X_train, y_train)
y_pred_log = log_model.predict(X_test) # 3. Decision Tree (The "Flexible" Non-Linear Model)
tree_model = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)
plt.figure(figsize=(10,6))
plot_tree(tree_model, feature_names=X.columns, class_names=['Fail', 'Pass'], filled=True)
plt.show()