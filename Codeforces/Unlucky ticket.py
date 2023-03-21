n = int(input())
x = input()
full = [int(i) for i in x]
first, second = [0] * n, [0] * n
lucky1, lucky2 = True, True
for i in range(n):
    first[i] = full[i]
    second[i] = full[2 * n - i - 1]

first.sort(), second.sort()

for i in range(n):
    if lucky1 and first[i] > second[i]:
        lucky1 = True
    else:
        lucky1 = False
    if lucky2 and first[i] < second[i]:
        lucky2 = True
    else:
        lucky2 = False
    if not lucky1 and not lucky2:
        break
if lucky1 or lucky2:
    print("YES")
else:
    print("NO")
