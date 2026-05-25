import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC # 1. Load and Preprocess
df = pd.read_csv('troubleshooting_data.csv')
df.fillna(df.median(), inplace=True) # Handle missing values
X = df.drop('problem_type', axis=1)
y = df['problem_type'] # 2. Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 3. Model Training & Comparison
models = {"LogReg": LogisticRegression(max_iter=1000), "DecTree": DecisionTreeClassifier(), "SVM": SVC(probability=True)}
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    results[name] = acc
    print(f"{name} Accuracy: {acc*100:.2f}%") # 4. Visualization of Results
sns.barplot(x=list(results.keys()), y=list(results.values()))
plt.title('Model Performance Comparison')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.show()