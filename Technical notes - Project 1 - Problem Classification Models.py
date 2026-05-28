import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# 1. Load Data
df = pd.read_csv('troubleshooting_data.csv')

# Protect ground truth: Drop rows missing the target variable completely
df.dropna(subset=['problem_type'], inplace=True)

X = df.drop('problem_type', axis=1)
y = df['problem_type']

# Handle missing values strictly on features
X.fillna(X.median(), inplace=True)

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features for Logistic Regression and SVM
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Model Training & Comparison
models = {
    "LogReg": LogisticRegression(max_iter=1000), 
    "DecTree": DecisionTreeClassifier(), 
    "SVM": SVC(probability=True)
}
results = {}

for name, model in models.items():
    # Use scaled features for distance/gradient models, raw for trees
    X_tr = X_train if name == "DecTree" else X_train_scaled
    X_te = X_test if name == "DecTree" else X_test_scaled
    
    model.fit(X_tr, y_train)
    preds = model.predict(X_te)
    acc = accuracy_score(y_test, preds)
    results[name] = acc
    print(f"{name} Accuracy: {acc*100:.2f}%")
