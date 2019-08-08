import random

n = 1000
cnt = 0

for i in range(n):
    x = random.random()
    y = random.random()
    if x * x + y * y <= 1:
        cnt += 1

print(cnt / n)