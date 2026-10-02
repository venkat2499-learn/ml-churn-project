What business problem were you solving?
We were predicting whether a customer will churn or not.

Why is this a classification problem?
It is a classification problem because the model predicts two categories: churned (1) or not churned (0).

What were the features?
The features were monthly_charge, months_as_customer, support_tickets, and weekly_usage_hours.

What was the target?
The target was churned.

Why did we check for missing values before training?
We checked for missing values because missing data can affect the model's learning and predictions.

Why did we split the data into training and testing sets?
We split the data to train the model on one part and test how well it works on new data.

What exactly happened when model.fit() ran?
model.fit() trained the model by learning patterns from the features and target in the training data.

What did model.predict() do?
model.predict() used the learned patterns to predict whether customers would churn.

What was your first test accuracy?
The first test accuracy was 0.75 (75%).

What happened after changing max_depth?
The accuracy improved from 0.75 to 0.85 when max_depth changed from 2 to 4.

Did the model make any incorrect predictions?
Yes, the model made some incorrect predictions.

Why should an ML project be treated as an iterative process?
Because we can test, improve, and adjust the model based on its results instead of training it only once.

How many rows are in the dataset?
There are 80 rows in the dataset.

How many columns are there?
There are 5 columns in the dataset.

Which columns contain missing values?
The columns with missing values are
support_tickets → 2 missing values
weekly_usage_hours → 1 missing value

Which column is the target?
The target column is churned.

Why is churned not included inside X?
churned is not included in X because it is the answer we want the model to predict.
X = clues/features
y = answer/target
So, churned goes into y, not X.

Example of a correct prediction:
Actual: 0, Predicted: 0 — the model correctly predicted that the customer did not churn.

Example of an incorrect prediction:
Actual: 1, Predicted: 0 — the model predicted that the customer would not churn, but the customer actually churned.

What does the incorrect prediction remind you about Machine Learning?
Machine Learning can make mistakes and is not always 100% accurate.

Model 1
max_depth = 2
Test accuracy = 0.75

Model 2
max_depth = 4
Test accuracy: 0.85

Which model performed better?
Model 2 performed better.

Did changing the model setting improve the result?
Yes, it improved the result.

Did it stay the same?
No, it did not stay the same. The accuracy improved from 0.75 to 0.85

Did it become worse?
No, it did not become worse. The accuracy improved from 0.75 to 0.85.

If training accuracy becomes extremely high but test accuracy is lower, what might that tell us?
The model may be overfitting. It learned the training data very well but does not perform as well on new data.