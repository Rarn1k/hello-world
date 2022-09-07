from collections import Counter

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

train = pd.read_csv('https://stepik.org/media/attachments/course/4852/invasion.csv')
x = train.drop('class', axis=1)
y = train['class'].map({'transport': 0, 'fighter': 1, 'cruiser': 2})
parameters = {'n_estimators': range(10, 50, 10), 'max_depth': range(1, 12, 2), 'min_samples_leaf': range(1, 7),
              'min_samples_split': range(2, 9, 2)}
rf = RandomForestClassifier(random_state=0)
search = GridSearchCV(rf, parameters, cv=3, n_jobs=-1)
search.fit(x, y)
best_forest = search.best_estimator_
test = pd.read_csv('https://stepik.org/media/attachments/course/4852/operative_information.csv')
print(Counter(best_forest.predict(test)))
