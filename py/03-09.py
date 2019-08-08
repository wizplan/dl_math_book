import numpy as np

A = np.array([[2, 3], [-1, 4]])
B = np.array([7, 2])

print(np.linalg.inv(A) @ B)