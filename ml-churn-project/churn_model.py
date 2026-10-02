import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv("customer_churn.csv")

data["support_tickets"] = data["support_tickets"].fillna(
    data["support_tickets"].median()
)
data["weekly_usage_hours"] = data["weekly_usage_hours"].fillna(
    data["weekly_usage_hours"].median()
)

X = data[
    [
        "monthly_charge",
        "months_as_customer",
        "support_tickets",
        "weekly_usage_hours",
    ]
]
y = data["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42,
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

results = X_test.copy()
results["actual"] = y_test.values
results["predicted"] = predictions

print(results[["actual", "predicted"]])
print("\nTest accuracy:", round(accuracy, 3))