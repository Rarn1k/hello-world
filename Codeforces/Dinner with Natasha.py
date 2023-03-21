n, m = [int(_) for _ in input().split()]
rests = []
prospect, street = 0, 0
for _ in range(n):
    rests.append([int(_) for _ in input().split()])
min_in_prospects = [rests[i][0] for i in range(n)]

for i in range(n):
    for j in range(m):
        if min_in_prospects[i] > rests[i][j]:
            min_in_prospects[i] = rests[i][j]

for i in range(n):
    if min_in_prospects[i] > min_in_prospects[prospect]:
        prospect = i

for j in range(m):
    if rests[prospect][j] < rests[prospect][street]:
        street = j

print(rests[prospect][street])
