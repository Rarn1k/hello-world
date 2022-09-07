import pandas as pd
import numpy as np

#my_stat = pd.read_csv("https://stepik.org/media/attachments/course/4852/my_stat.csv")
# typeee = {"type": ['A', 'A', 'B', 'B'], "value": [10, 14, 12, 23]}
# my_data = pd.DataFrame(typeee)
# print(my_data)
#
#
# subset_1 = my_stat.iloc[0:9, [0, 2]]
# subset_2 = my_stat.iloc[:, [1, 3]].drop([0, 4], axis=0)

# subset_1 = my_stat.query('V1 > 0 & V3 == "A"')
# subset_2 = my_stat.query('V2 != 10 | V4 >= 1')

# print(subset_1)
# print(subset_2)
# my_stat['V5'] = my_stat['V1'] + my_stat['V4']
# my_stat['V6'] = np.log(my_stat['V2'])

#my_stat = my_stat.rename(columns={'V1': 'session_value', 'V2': 'group', 'V3': 'time', 'V4': 'n_users'})

my_stat = pd.read_csv("https://stepik.org/media/attachments/course/4852/my_stat_1.csv")
# my_stat = my_stat.fillna(0)
# my_stat_2 = my_stat[my_stat.n_users >= 0]
# m = my_stat_2['n_users'].median()
# my_stat.loc[my_stat['n_users'] < 0, 'n_users'] = m

mean_session_value_data = my_stat.groupby('group', as_index=False)\
    .agg({'session_value': 'mean'}).rename(index=str, columns={'session_value': 'mean_session_value'})
#mean_session_value_data.rename(columns={'session_value': 'mean_session_value'})
print(mean_session_value_data)
