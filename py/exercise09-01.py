import numpy as np
from sklearn import linear_model

lr = linear_model.LinearRegression()
x = np.array([[0], [2], [3], [5], [6], [7], [9], [11]])
y = np.array([1.5, 1.7, 2.1, 2.2, 2.8, 2.9, 3.2, 3.7])

# 예측 모델에 적용
lr.fit(x, y)

# 회귀계수
print(lr.coef_)

# 절편
print(lr.intercept_)

# 결정계수
print(lr.score(x, y))