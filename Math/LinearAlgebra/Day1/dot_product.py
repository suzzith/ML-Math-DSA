def dot_product(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

# Test
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print("Dot Product:", dot_product(v1, v2))  # Output: 32
