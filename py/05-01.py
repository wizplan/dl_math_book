data = [[0, 1.5], [2, 1.7], [3, 2.1], [5, 2.2], [6, 2.8], [7, 2.9], [9, 3.2], [11, 3.7]]

def dEa(a, b):
    sum_value = 0
    for i in data:
        sum_value += i[0] * (a * i[0] + b - i[1])

    return sum_value

def dEb(a, b):
    sum_value = 0
    for i in data:
        sum_value += a * i[0] + b - i[1]

    return sum_value

eta = 0.006   # 학습률 설정
a, b = 2, 1   # 경사하강법을 시작하는 기울기값과 절편

# 오차 제곱의 합이 최소일 때의 a, b 계산
for i in range(0, 200):
    a += - eta * dEa(a, b)
    b += - eta * dEb(a, b)
    print([a, b])