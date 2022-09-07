import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

train = pd.read_csv('https://stepik.org/media/attachments/course/4852/train_data_tree.csv')
x_train = train.drop('num', axis=1)
y_train = train.num
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(x_train, y_train)
tree.plot_tree(clf, filled=True)
plt.show()
l_node = clf.tree_.children_left[0]
r_node = clf.tree_.children_right[0]
n0 = clf.tree_.n_node_samples[l_node]
e0 = clf.tree_.impurity[l_node]
n1 = clf.tree_.n_node_samples[r_node]
e1 = clf.tree_.impurity[r_node]
n = n0 + n1
ig = round(0.996 - (n0 * e0 + n1 * e1) / n, 3)
print(ig)
