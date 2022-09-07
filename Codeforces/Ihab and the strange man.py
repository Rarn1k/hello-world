size = int(input())
arr = [int(_) for _ in input().split()]
equal = True
chet = 0
for i in range(1, size):
    if arr[0] % 2 == 0:
        if arr[i] % 2 == 1:
            equal = False
            break
    if arr[0] % 2 == 1:
        if arr[i] % 2 == 0:
            equal = False
            break
if equal:
    print(*arr)
else:
    print(*sorted(arr))
