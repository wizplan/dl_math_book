def f(x, y):
    return x * x + y * y

def dfx(x, y):
    return 2 * x

def dfy(x, y):
    return 2 * y

eta = 0.1      # 학습률 설정
x, y = 10, 8   # 경사하강법을 시작하는 그래프상의 점 설정
print(f(x, y))

# 최솟값인 점으로 이동
for i in range(0, 30):
    x += - eta * dfx(x, y)
    y += - eta * dfy(x, y)
    print(f(x, y))