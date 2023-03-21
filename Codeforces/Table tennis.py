from collections import deque
n, k = [int(_) for _ in input().split()]
counter = 1
a = deque()
[a.append(int(_)) for _ in input().split()]
first = a.popleft()
second = a.popleft()
winner = max(first, second)
a.append(min(first, second))

for i in range(n):
    if winner > a[0]:
        counter += 1
        data = a.popleft()
        a.append(data)
    else:
        counter = 1
        a.append(winner)
        winner = a.popleft()
    if counter == k:
        break
print(winner)
