def add_vectors(a, b):
    return [a[i] + b[i] for i in range(len(a))]

# Test it
v1 = [2, 4, 6]
v2 = [1, 3, 5]
print("Sum:", add_vectors(v1, v2))  # Output: [3, 7, 11]
