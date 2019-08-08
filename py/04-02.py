# 함수 정의
def f(x):
    return x ** 2

# 미분
def df(x, h):
    return (f(x + h) - f(x)) / h

# 다른 미분 방법
# def df(x, h):
#    return (f(x + h) - f(x - h)) / (2 * h)

# h값을 0에 가깝게 변화시켜 x = 0일 때와 1일 때의 미분계수 계산
for h in [1, 1e-1, 1e-2, 1e-3]:
    print([h, df(0, h), df(1, h)])