import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
B = np.array([[3, 4], [4, 5], [5, 6]])

print(A.dot(B))   # 행렬의 곱 계산

C = np.matrix([[1, 2, 3], [3, 4, 5]])
D = np.matrix([[3, 4], [4, 5], [5, 6]])

print(C * D)      # matrix 함수를 사용한 행렬의 곱 계산
print(A @ B)      # 파이썬 3.5 이후에 포함된 @ 연산자 사용