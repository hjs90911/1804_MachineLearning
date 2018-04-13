from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

X, y = make_moons(n_samples=100, noise=0.25, random_state=3)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                    random_state=42)

mlp = MLPClassifier(solver='lbfgs', random_state=0)
mlp.fit(X_train, y_train)
print(mlp.score(X_test, y_test))

####################################################################
mlp = MLPClassifier(solver='lbfgs', random_state=0,
                    hidden_layer_sizes=[10,10])
mlp.fit(X_train, y_train)
print(mlp.score(X_test,y_test))