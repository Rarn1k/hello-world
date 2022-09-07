n, length = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
a.sort()
max_dist = 0
for i in range(n - 1):
    if a[i + 1] - a[i] > max_dist:
        max_dist = a[i + 1] - a[i]
print(max(max_dist / 2, max(a[0] - 0, length - a[n - 1])))
