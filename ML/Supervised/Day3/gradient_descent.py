x = [1, 2, 3, 4]  # Inputs
y = [2, 4, 6, 8]  # Actual output

m = 0  # Start with guess: slope = 0
b = 0  # Start with guess: intercept = 0
lr = 0.01  # Step size (learning rate)
epochs = 1000  # Number of steps we take

n = len(x)

for _ in range(epochs):  # Take 1000 steps
    y_pred = [m * xi + b for xi in x]  # Predict y values
    error = [y[i] - y_pred[i] for i in range(n)]  # Difference from real y

    # Partial derivatives (gradients)
    dm = -(2/n) * sum([x[i] * error[i] for i in range(n)])
    db = -(2/n) * sum(error)

    # Update m and b (go down the hill)
    m -= lr * dm
    b -= lr * db

print("Final slope (m):", m)
print("Final intercept (b):", b)
