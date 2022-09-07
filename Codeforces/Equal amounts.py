k = int(input())
triple = list()
exist = False
for i in range(k):
    n = int(input())
    sequence = [int(_) for _ in input().split()]
    summa = sum(sequence)
    for t in range(n):
        triple.append([summa - sequence[t], i + 1, t + 1])

triple.sort()
for i in range(len(triple) - 1):
    if triple[i][1] != triple[i + 1][1] and triple[i][0] == triple[i + 1][0]:
        print('YES' + '\n' + str(triple[i][1]) + ' ' + str(triple[i][2]) + '\n' + str(triple[i + 1][1]) + ' '
              + str(triple[i + 1][2]))
        exist = True
        break
if not exist:
    print('NO')
