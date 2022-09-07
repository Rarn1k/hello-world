import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

train = pd.read_csv('https://stepik.org/media/attachments/course/4852/training_mush.csv')
train = train.rename(columns={'class': 'cl'})
x = train.drop('cl', axis=1)
y = train.cl
parameters = {'n_estimators': range(10, 50, 10), 'max_depth': range(1, 12, 2), 'min_samples_leaf': range(1, 7),
              'min_samples_split': range(2, 9, 2)}
rf = RandomForestClassifier(random_state=0)
search = GridSearchCV(rf, parameters, cv=3, n_jobs=-1)
search.fit(x, y)
best_forest = search.best_estimator_
test = pd.read_csv('https://stepik.org/media/attachments/course/4852/testing_mush.csv')
y_pred = best_forest.predict(test)
y_true = pd.read_csv('testing_y_mush.csv')
conf_matr = confusion_matrix(y_true, y_pred)
sns.heatmap(conf_matr, annot=True, cmap="Blues")
plt.show()
