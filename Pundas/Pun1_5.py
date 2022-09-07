import pandas as pd
import numpy as np
st = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
print(st[st['lunch'] == 'free/reduced'].shape[0] / st.shape[0])
print(st.describe() - st[st['lunch'] == 'free/reduced'].describe())
