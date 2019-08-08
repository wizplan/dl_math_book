import random
import collections
import math

r = []   # 난수를 1,000개 생성하고 리스트에 저장

for i in range(1000):
    r.append(random.random())

# 소수점 첫 번째 자리 기준으로 난수를 구분
print(collections.Counter([math.floor(x * 10) for x in r]))