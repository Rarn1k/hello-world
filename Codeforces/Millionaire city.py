n, s = [int(_) for _ in input().split()]
towns = list()
distance = list()
exist = False
last_town = -1
for _ in range(n):
    x, y, k = [int(_) for _ in input().split()]
    towns.append((x, y, k))
    dist = (x ** 2 + y ** 2) ** 0.5
    distance.append((dist, k))
distance.sort()
for i in range(n):
    s += distance[i][1]
    if s >= 10 ** 6:
        last_town = i
        exist = True
        break
if exist:
    print(distance[last_town][0])
else:
    print(-1)
