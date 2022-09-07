n, m = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
a.sort()
answer = []
for element in b:
    left = -1
    right = n
    while right - left > 1:
        m = (right + left) // 2
        if a[m] <= element:
            left = m
        else:
            right = m
    answer.append(right)
print(*answer)
