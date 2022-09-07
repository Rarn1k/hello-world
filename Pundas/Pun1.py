import pandas as pd
import numpy as np
st = pd.read_csv('https://stepik.org/media/attachments/course/4852/titanic.csv')
print(st.shape)
print(st.dtypes.value_counts())
