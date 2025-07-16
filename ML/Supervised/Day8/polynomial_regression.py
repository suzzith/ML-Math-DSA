import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Create dummy data (non-linear)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([3, 6, 19, 38, 89, 164])

# Transform features to polynomial degree 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit Linear Regression on transformed data
model = LinearRegression()
model.fit(X_poly, y)

# Predict
y_pred = model.predict(X_poly)

# Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Polynomial Fit')
plt.title("Polynomial Regression (Degree 2)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Evaluation
print("MSE:", mean_squared_error(y, y_pred))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
