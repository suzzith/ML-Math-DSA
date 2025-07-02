import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [50, 55, 65, 70, 75]

# Slope and Intercept (already calculated)
m = 6.5
b = 45

# Predict Y values
predicted_y = [m * x + b for x in X]

# Plot
plt.scatter(X, Y, color='blue', label='Original Data')
plt.plot(X, predicted_y, color='red', label='Best Fit Line')
plt.xlabel("Hours")
plt.ylabel("Score")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
