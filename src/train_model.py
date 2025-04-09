import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Load train-test data
with open("../data/processed/tfidf_features.pkl", "rb") as f:
    X = pickle.load(f)

with open("../data/processed/labels.pkl", "rb") as f:
    y = pickle.load(f)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Step 1: Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ✅ Step 2: Evaluate Model
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

print(f"🔹 Train Accuracy: {train_accuracy:.4f}")
print(f"🔹 Test Accuracy: {test_accuracy:.4f}")

# ✅ Step 3: Additional Metrics
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# ✅ Step 4: Save the trained model
with open("../models/logistic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved successfully!")