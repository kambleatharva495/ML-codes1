# Sample Dataset
X = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 4, 6, 8, 10, 12, 14, 16]

# Splitting Dataset (75% Training, 25% Testing)
X_train = X[:6]
X_test = X[6:]

y_train = y[:6]
y_test = y[6:]

# Model Training (Linear Regression Manually)
n = len(X_train)

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_x += X_train[i]
    sum_y += y_train[i]
    sum_xy += X_train[i] * y_train[i]
    sum_x2 += X_train[i] * X_train[i]

# Calculate slope (m) and intercept (c)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

c = (sum_y - m * sum_x) / n

# Prediction on Test Data
y_pred = []

for x in X_test:
    prediction = m * x + c
    y_pred.append(prediction)

# Display Results
print("Training Data:", X_train)
print("Testing Data:", X_test)
print("Actual Values:", y_test)
print("Predicted Values:", y_pred)

# Model Evaluation (Mean Squared Error)
error = 0

for i in range(len(y_test)):
    error += (y_test[i] - y_pred[i]) ** 2

mse = error / len(y_test)

print("Mean Squared Error:", mse)