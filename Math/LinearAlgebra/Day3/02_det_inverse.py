#determinant  
 
import numpy as np

A = np.array([[4, 6], [3, 8]])
det = np.linalg.det(A)

print("Determinant:", det)



#inverse_matrix

A = np.array([[4, 7], [2, 6]])

inv_A = np.linalg.inv(A)
print("Inverse of A:")
print(inv_A)


