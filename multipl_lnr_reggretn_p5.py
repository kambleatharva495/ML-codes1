# Dataset (Area, Rooms, Age)
X = [
    [1000, 2, 10],
    [1500, 3, 8],
    [1800, 4, 5],
    [2000, 4, 3],
    [2200, 5, 2]
]

# House Prices
y = [200000, 300000, 400000, 450000, 500000]

# Initial values
b0 = 0
b1 = 0
b2 = 0
b3 = 0

learning_rate = 0.0000001
epochs = 10000
n = 5

# Scale area to make training easier
for i in range(n):
    X[i][0] = X[i][0] / 1000

# Scale prices
for i in range(n):
    y[i] = y[i] / 100000

# Model Training using Gradient Descent
for epoch in range(epochs):

    d0 = d1 = d2 = d3 = 0

    for i in range(n):
        area, rooms, age = X[i]

        prediction = b0 + b1*area + b2*rooms + b3*age

        error = prediction - y[i]

        d0 += error
        d1 += error * area
        d2 += error * rooms
        d3 += error * age

    # Update coefficients
    b0 -= learning_rate * d0 / n
    b1 -= learning_rate * d1 / n
    b2 -= learning_rate * d2 / n
    b3 -= learning_rate * d3 / n

# Prediction for new house
area = 2100 / 1000
rooms = 4
age = 3

predicted_price = b0 + b1*area + b2*rooms + b3*age

# Convert price back to original scale
predicted_price = predicted_price * 100000

print("Predicted Price:", predicted_price)