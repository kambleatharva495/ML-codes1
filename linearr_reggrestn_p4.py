# In [1]:
import numpy as np
import matplotlib.pyplot as plt

# In [2]:
# Dataset: Experience (years) aur Salary (thousand)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([30, 35, 42, 46, 52, 58, 61, 68, 74, 80])

print("Experience:", X)
print("Salary    :", y)

# In [3]:
# Mean nikalna
x_mean = np.mean(X)
y_mean = np.mean(y)

print("Mean of X:", x_mean)
print("Mean of y:", y_mean)

# In [4]:
# Slope (m) aur intercept (c) nikalna
# m = sum((x - x_mean)(y - y_mean)) / sum((x - x_mean)^2)
# c = y_mean - m * x_mean

m = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean) ** 2)
c = y_mean - m * x_mean

print("Slope (m)    :", round(m, 4))
print("Intercept (c):", round(c, 4))
print("Equation: y =", round(m, 2), "* x +", round(c, 2))

# In [5]:
# Prediction
y_pred = m * X + c

print("Actual   :", y)
print("Predicted:", np.round(y_pred, 2))

# In [6]:
# Model evaluation
mse = np.mean((y - y_pred) ** 2)
rmse = np.sqrt(mse)
r2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y_mean) ** 2)

print("MSE     :", round(mse, 4))
print("RMSE    :", round(rmse, 4))
print("R2 Score:", round(r2, 4))
 
# In [7]:
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.title('Linear Regression')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary (Thousand)')
plt.legend()
plt.show()

# In [8]:
# Naye data par prediction
new_exp = 12
print("Predicted salary for", new_exp, "years:", round(m * new_exp + c, 2))