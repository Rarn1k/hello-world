import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv("dataset_209770_6 (2).txt", sep=" ")
# print(df.plot.scatter(x='x', y='y'))
# plt.show()
#
# gen = pd.read_csv('genome_matrix.csv', index_col=0)
# g = sns.heatmap(gen, cmap="viridis")
# g.xaxis.set_ticks_position('top')
# g.xaxis.set_tick_params(rotation=90)
# print(g)
# plt.show()
#
# dota = pd.read_csv("https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv")
# print(dota['roles'].mode())

flowers = pd.read_csv("https://stepik.org/media/attachments/course/4852/iris.csv")
print(flowers.columns)
flowers.drop(flowers.columns[[0]], axis=1, inplace=True)
#sns.kdeplot(data=flowers)
#sns.violinplot(data=flowers["petal length"], axic=1, orient="v")
sns.pairplot(flowers)
plt.show()
