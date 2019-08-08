import numpy as np

# 입력 데이터
x = np.array([[0, 1, 2, 1, 0, 0], [0, 0, 1, 2, 1, 0], [0, 0, 0, 1, 2, 1], [0, 0, 0, 1, 3, 2], [1, 1, 1, 3, 2, 0], [2, 2, 3, 2, 1, 0]])

# 필터
f = np.array([[0, 1, 1], [0, 1, 1], [0, 1, 1]])

result = []

for i in range(len(x) - len(f) + 1):
    row = []
    for j in range(len(x[0]) - len(f[0]) + 1):
        # 행렬 요소끼리 곱한 후 합 계산
        row.append(np.sum(x[i:i + len(f), j:j + len(f[0])] * f))
    result.append(row)

print(result)