# linear_regression_scratch.py

# Sample Data
X = [1, 2, 3, 4, 5]
Y = [50, 55, 65, 70, 75]

# Step 1: Calculate mean
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

# Step 2: Calculate slope (m)
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2

m = numerator / denominator

# Step 3: Calculate intercept (b)
b = mean_y - m * mean_x

# Final line: y = mx + b
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Predict
def predict(x):
    return m * x + b

print("Prediction for 6 hrs study:", predict(6))
