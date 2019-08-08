import numpy as np

a = [[3, -2], [4, 5]]
b = [[1, -3, 4], [-2, 5, 3], [2, -1, 0]]
c = [[-1, 5, 2, -3], [0, 3, -1, 4], [2, -3, 0, -5], [-4, 2, 3, 1]]

print(np.linalg.inv(a))
print(np.linalg.inv(b))
print(np.linalg.inv(c))