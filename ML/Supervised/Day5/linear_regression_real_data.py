import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data.csv")

# Features and Labels
X = df[['Experience']]
y = df['Salary']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Evaluate
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("MSE:", mse)
print("R² Score:", r2)
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

# Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted Line')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.legend()
plt.title('Experience vs Salary')
plt.show()
