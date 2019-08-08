import numpy as np

# 상태 설정
S = np.array([0, 1, 2, 3])

# 상태 이동 전과 상태 이동 후를 0과 1로 설정
A = np.array([0, 1])

# 각 상태에서 이동했을 때 보상 설정
R = np.array([[1, -20], [4, -1], [0, 25], [0, 0]])

# 이동 경로 설정
S1 = np.array([[1, 2], [3, 0], [0, 3], [None, None]])

# 이동 확률
p = 0.5

# 학습률
alpha = 0.01

# 할인율
gamma = 0.8

# 학습 횟수
n = 3000

# 행동 가치 함수 초기화
Q = np.zeros(R.shape)

# 확률에 따라 상태 이동 여부 결정
def pi(p):
    if np.random.uniform(0, 1) <= p:
        return 0   # 상태 이동 전임을 반환
    else:
        return 1   # 상태 이동 후임을 반환

def q_learning():
    s = S[0]
    a = 0
    while S1[s, a] != None:
        a = pi(p)
        max_q = max(Q[S1[s, a], 0], Q[S1[s, a], 1])
        td = R[s, a] + gamma * max_q - Q[s, a]
        Q[s, a] += alpha * td
        s = S1[s, a]
    print(Q[0, 0], Q[0, 1])

# 설정한 학습 횟수만큼 Q 학습 진행
for i in range(n):
    q_learning()