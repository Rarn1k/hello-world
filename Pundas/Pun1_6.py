import pandas as pd
import numpy as np
st = pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')
print(st.groupby('legs').describe())

buh = pd.read_csv('https://stepik.org/media/attachments/course/4852/accountancy.csv')
print(buh.groupby(['Type', 'Executor'], as_index=False).aggregate({'Salary' : 'mean'}))

print(st.groupby(['attack_type', 'primary_attr']).count())

al = pd.read_csv('http://stepik.org/media/attachments/course/4852/algae.csv')
print(*al.query("genus == 'Fucus'").alanin.describe().loc[['min', 'mean', 'max']].values.round(2))
print(al.groupby('group').describe())
