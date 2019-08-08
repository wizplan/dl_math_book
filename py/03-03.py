import numpy as np
import math

a = np.array([3, 2])
b = np.array([1, 4])

print(a + b)               # 벡터의 합
print(a - b)               # 벡터의 차
print(np.linalg.norm(a))   # 벡터 a의 크기
print(np.linalg.norm(b))   # 벡터 b의 크기

# 벡터의 크기를 함수로 계산
def norm(x):
    return math.sqrt(sum([i ** 2 for i in x]))

print(norm(a))             # 벡터 a의 크기
print(norm(b))             # 벡터 b의 크기