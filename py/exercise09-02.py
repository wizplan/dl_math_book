import numpy as np
from sklearn import linear_model

lr = linear_model.LinearRegression()
x = [[-2.1, -3.6], [-1.4, 3.1], [0.1, -2.7], [0.8, 1.8], [1.7, -0.5], [3.2, 4.1], [5.7, -1.9], [6.2, 5.2]]
y = [-6.8, 12.2, -8.3, 3.6, -4.8, 5.8, -17.2, 3.1]

# 예측 모델에 적용
lr.fit(x, y)

# 회귀계수
print(lr.coef_)

# 절편
print(lr.intercept_)

# 결정계수
print(lr.score(x, y))