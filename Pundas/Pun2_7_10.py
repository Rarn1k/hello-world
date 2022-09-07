import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

x_train = train.drop('y', axis=1)
y_train = train.y
dt = DecisionTreeClassifier()
ps = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10), 'min_samples_leaf': range(1, 10)}
search = GridSearchCV(dt, ps, cv=5)
search.fit(x_train, y_train)
best_tree = search.best_estimator_
predictions = best_tree.predict(test)
