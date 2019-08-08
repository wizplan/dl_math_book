import numpy as np

# 입력
x = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 1, 2, 1, 0, 0], [0, 1, 2, 1, 0, 0], [1, 2, 2, 2, 1, 0], [1, 2, 3, 2, 1, 0]])

result = []

for i in range(0, len(x), 2):
    row = []
    for j in range(0, len(x[0]), 2):
        # 구분한 영역의 최댓값 계산
        row.append(np.max(x[i:i + 2, j:j + 2]))
    result.append(row)

print(result)