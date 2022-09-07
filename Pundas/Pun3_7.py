from time import time

import numpy as np
import pandas as pd

df = pd.read_csv('https://stepik.org/media/attachments/course/4852/iris.csv')
before = time()
df.apply(np.mean)
after = time()
print(after - before)
before = time()
df.mean(axis=0)
after = time()
print(after - before)
before = time()
var = df.describe().loc['mean']
after = time()
print(after - before)
before = time()
df.apply('mean')
after = time()
print(after - before)