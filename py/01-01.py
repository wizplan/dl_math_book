from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# 붓꽃 데이터 세트 검색
iris = load_iris()
x, y = iris.data, iris.target

# 학습 데이터와 테스트 데이터로 나눔
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

# 초기화
nn = MLPClassifier(solver="sgd", random_state=0, max_iter=10000)

# 학습
nn.fit(x_train, y_train)

# 예측 결과 확인
print("result:", nn.score(x_test, y_test))