import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

train = pd.read_csv('https://stepik.org/media/attachments/course/4852/training_mush.csv')
train = train.rename(columns={'class': 'cl'})
x = train.drop('cl', axis=1)
y = train.cl
parametrs = {'n_estimators': range(10, 50, 10), 'max_depth': range(1, 12, 2), 'min_samples_leaf': range(1, 7),
             'min_samples_split': range(2, 9, 2)}
rf = RandomForestClassifier(random_state=0)
search = GridSearchCV(rf, parametrs, cv=3, n_jobs=-1)
search.fit(x, y)
best_forest = search.best_estimator_
imp = pd.DataFrame(best_forest.feature_importances_, index=x.columns, columns=['importance'])
imp.sort_values('importance').plot(kind='barh', figsize=(12, 8))
plt.show()
