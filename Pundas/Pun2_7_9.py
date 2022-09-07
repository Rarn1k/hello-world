import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
dt = DecisionTreeClassifier()
ps = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10), 'min_samples_leaf': range(1, 10)}
search = RandomizedSearchCV(dt, ps)
search.fit(X, y)
best_tree = search.best_estimator_
