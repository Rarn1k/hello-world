n, k = [int(_) for _ in input().split()]
n1 = n
arr = []
mul = 1
i = 2
while i <= n:
    if n % i == 0:
        arr.append(i)
        n //= i
        i -= 1
    i += 1

if len(arr) > k:
    while len(arr) != k:
        mul = arr[len(arr) - 1]
        arr.pop()
        arr[0] *= mul
if len(arr) == k:
    print(*arr)
else:
    print(-1)
