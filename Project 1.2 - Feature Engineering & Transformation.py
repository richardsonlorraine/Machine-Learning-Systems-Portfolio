# Fix: Define feature column configurations explicitly
numerical_features = ["age", "income", "transaction_amount"]
categorical_features = ["device_type", "region"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_features), 
    # Operational tip: handle_unknown='ignore' prevents crashes on unseen production data
    ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_features) 
])
