number_of_tests = int(input())
for _ in range(number_of_tests):
    size = int(input())
    arr = [int(_) for _ in input().split()]
    arr.sort()
    neighbors = [int(0) for _ in range(size)]
    i, j = len(arr) // 2 - 1, len(arr) // 2
    t, k = 0, 1
    while i >= 0 and j < len(arr):
        neighbors[k] = arr[i]
        neighbors[t] = arr[j]
        t += 2
        k += 2
        i -= 1
        j += 1
    print(*neighbors)
#########################################