import numpy as np

# 가중치 초깃값 설정
V = np.array([[0.1, 0.3], [0.2, 0.4]])
W = np.array([[0.1, 0.3], [0.2, 0.4]])

# 지도 데이터
t = np.array([[1, 0]])

# 학습률
eta = 0.005

# 순전파
x = np.array([[1, 0.5]])
y = x.dot(V)
z = y.dot(W)

# 역전파
delta2 = z - t
grad_W = y.T.dot(delta2)
delta1 = delta2.dot(W.T)
grad_V = x.T.dot(delta1)
W -= eta * grad_W
V -= eta * grad_V
print(V)
print(W)