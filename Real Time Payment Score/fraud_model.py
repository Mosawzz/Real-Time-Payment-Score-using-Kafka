import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    'amount': [100, 200, 250, 300, 500, 700, 50],
    'is_fraud': [0, 0, 0, 0, 1, 1, 0]  # 0 = legitimate, 1 = fraud
})

X = data[['amount']]
y = data['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))


joblib.dump(model, "model/fraud_model.pkl")
