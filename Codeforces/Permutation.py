n = int(input())
a = [int(_) for _ in input().split()]
a.sort()
counter = 0
for i in range(n - 1):
    if a[i] > n or a[i] == a[i + 1]:
        counter += 1
if a[n - 1] > n:
    counter += 1
print(counter)
