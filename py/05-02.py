import numpy as np

data = [[0, 0], [2, 0], [3, 0], [5, 0], [6, 1], [7, 1], [9, 1], [11, 1]]

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def dEa(a, b):
    sum_value = 0
    for i in data:
        sum_value += i[0] * (sigmoid(a * i[0] + b) - i[1])

    return sum_value

def dEb(a, b):
    sum_value = 0
    for i in data:
        sum_value += sigmoid(a * i[0] + b) - i[1]

    return sum_value

eta = 0.5     # 학습률 설정
a, b = 2, 1   # 경사하강법을 시작하는 기울기값과 절편

# 최솟값으로 이동했을 때의 결정 경계 계산
for i in range(0, 200):
    a += - eta * dEa(a, b)
    b += - eta * dEb(a, b)
    print([-(b/a)])