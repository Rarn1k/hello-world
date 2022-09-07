import random


# def fant():
#     counter = 0
#     fants = [_ for _ in range(33)]
#     for _ in range(50000):
#         random.shuffle(fants)
#         if any(i == fants[i] for i in range(33)):
#             counter += 1
#     print(round(counter / 33, 3))


def fant():
    m = 50000
    n = 20
    counter = 0
    for _ in range(m):
        if all(map(lambda x, y: x - y, range(n), random.sample(range(n), n))):
            counter += 1
    print(round(counter / m, 3))


fant()
