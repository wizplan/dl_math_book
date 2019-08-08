import numpy as np

a = [[2, 5, -4], [3, -2, 6], [-1, 3, -2]]
b = [9, 9, 4]
print(np.linalg.inv(a) @ b)

x = [[-1, 3, 5, 2], [4, -6, 3, -1], [3, 3, -4, 3], [2, -1, 2, -4]]
y = [8, -32, 26, -25]
print(np.linalg.inv(x) @ y)