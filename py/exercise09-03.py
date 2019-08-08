import numpy as np
from sklearn import linear_model

lr = linear_model.LinearRegression()
x = [[-3.4, 5.1, 4.1], [-2.2, 3.7, -3.4], [-1.3, -1.6, 2.6], [0.4, 7.3, -1.4], [1.4, -6.1, -3.6], [2.9, 4.2, 3.5], [4.6, 3.9, 2.9], [6.1, 2.5, -1.1]]
y = [32.5, 16.1, 2.8, 19.1, -27.1, 4.8, -3.5, -17.5]

# 예측 모델에 적용
lr.fit(x, y)

# 회귀계수
print(lr.coef_)

# 절편
print(lr.intercept_)

# 결정계수
print(lr.score(x, y))