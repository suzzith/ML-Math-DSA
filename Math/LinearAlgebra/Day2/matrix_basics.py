import numpy as np

# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Transpose
print("Transpose of A:\n", A.T)

# Matrix Multiplication
print("A x B:\n", np.matmul(A, B))

# Identity Matrix
I = np.identity(2)
print("Identity:\n", I)
print("A x I:\n", np.matmul(A, I))
