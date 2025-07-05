##step 1: importing libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

##step 2: generate non-linear dataset

# Input data (X) and labels (y)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([3, 6, 14, 30, 55, 91, 140, 204, 285, 385])  # Clearly not linear

## step 3: fit linear regression

lin_model = LinearRegression()
lin_model.fit(X, y)

y_pred_linear = lin_model.predict(X)

##step 4:Fit Polynomial Regression (degree=3)

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

y_pred_poly = poly_model.predict(X_poly)


##step 5:Visualize Both

plt.scatter(X, y, color='red', label='Original Data')
plt.plot(X, y_pred_linear, color='blue', label='Linear Fit')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Fit (deg=3)')
plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.show()