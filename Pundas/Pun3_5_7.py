import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

train = pd.read_csv('https://stepik.org/media/attachments/course/4852/space_can_be_a_dangerous_place.csv')
sns.heatmap(train.corr(), cmap="Purples")
plt.show()
