import pandas as pd
import numpy as np
import seaborn as sns
import json
from sklearn import tree


df_tr = pd.read_csv('https://stepik.org/media/attachments/course/4852/dogs_n_cats.csv')

X = df_tr.drop(['Вид'], axis=1)
y = df_tr['Вид']
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)
x_test = pd.read_json('dataset_209691_15.txt')
result = clf.predict(x_test)
print(pd.Series(result)[result == 'собачка'].count())
