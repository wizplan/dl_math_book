import numpy as np

# 난수를 1,000개 생성한 리스트를 변수 n에 저장
n = np.random.randn(1000)

print(np.mean(n))   # 평균 계산
print(np.std(n))    # 표준편차 계산