n, m = [int(_) for _ in input().split()]
poland = set()
enemy = set()
for _ in range(n):
    poland.add(input())
for _ in range(m):
    enemy.add(input())
general = poland & enemy
n -= len(general)
m -= len(general)
if len(general) % 2 == 1:
    n += 1
if n > m:
    print('YES')
else:
    print('NO')
