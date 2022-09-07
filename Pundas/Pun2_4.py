import matplotlib.pyplot as plt
from sklearn import tree
import pandas as pd
import numpy as np
import seaborn as sns

df_train = pd.read_csv('https://stepik.org/media/attachments/course/4852/train_iris.csv')
df_test = pd.read_csv('https://stepik.org/media/attachments/course/4852/test_iris.csv')
X_train = df_train.drop(['species', 'Unnamed: 0'], axis=1)
X_test = df_test.drop(['species', 'Unnamed: 0'], axis=1)
y_train = df_train.species
y_test = df_test.species

rs = np.random.seed(0)
score_data = pd.DataFrame()
max_depth_values = range(1, 100)

for max_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth, random_state=rs)
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    temp_score_data = pd.DataFrame({'max_depth': [max_depth], 'train_score': [train_score], 'test_score': [test_score]})
    score_data = score_data.append(temp_score_data)

scores_data_long = pd.melt(score_data, id_vars=['max_depth'], value_vars=['train_score', 'test_score'],
                           var_name='set_type', value_name='score')
sns.lineplot(x='max_depth', y='score', hue='set_type', data=scores_data_long)
plt.show()
