import math

def var(data):
    avg = sum(data) / len(data)
    total = 0

    for i in data:
        total += (avg - i) ** 2

    return total / len(data)

def std(data):
    return math.sqrt(var(data))

a = [72, 61, 91, 31, 45]

print(sum(a) / len(a))   # 평균 출력
print(var(a))            # 분산 출력
print(std(a))            # 표준편차 출력