import numpy as np


def ent(p):
    q = 1 - p
    entr1 = -p * np.log2(p + 1e-10) - q * np.log2(q + 1e-10)
    return round(entr1, 2)


def ig(n1, n2, e1, e2, N):
    return 0.97 - n1/N * e1 + n2/N * e2


print(ent(4 / 9))
print(ent(4 / 5), "\n")
print(ig(9, 1, 0, 0.99, 10))
print(ig(5, 5, 0, 0.72, 10))
print(ig(4, 6, 0, 0, 10))
