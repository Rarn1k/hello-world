import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
precision = precision_score(y_test, predictions, average='micro')
