def matrix_multiply(A, B):
    result = [[0, 0],
              [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Test
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Product:", matrix_multiply(A, B))
