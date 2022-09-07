import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
dt = DecisionTreeClassifier()
parameters = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10), 'min_samples_leaf': range(1, 10)}
search = GridSearchCV(dt, parameters, cv=5)
search.fit(X, y)
best_tree = search.best_estimator_
