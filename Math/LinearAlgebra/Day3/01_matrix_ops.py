1. Matrix Addition
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Add A and B
result_add = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result_add.append(row)

print("Matrix Addition:")
for row in result_add:
    print(row)


2. Scalar Multiplication
k = 3
result_scalar = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(k * A[i][j])
    result_scalar.append(row)

print("\nScalar Multiplication (k=3):")
for row in result_scalar:
    print(row)

3. Matrix Multiplication
result_mult = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        sum_val = 0
        for k in range(len(B)):
            sum_val += A[i][k] * B[k][j]
        row.append(sum_val)
    result_mult.append(row)

print("\nMatrix Multiplication:")
for row in result_mult:
    print(row)

4. Transpose of a Matrix
transpose = []
for i in range(len(A[0])):  # loop over columns
    row = []
    for j in range(len(A)):  # loop over rows
        row.append(A[j][i])
    transpose.append(row)

print("\nTranspose of Matrix A:")
for row in transpose:
    print(row)

