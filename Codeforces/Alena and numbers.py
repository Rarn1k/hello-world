n, m = [int(_) for _ in input().split()]
counter = 0
mn1, mn2 = 0, 0
end = m
while (end + 1) % 5 != 0:
    end -= 1
end -= 1


for i in range(n):
    begin = 3 - i
    if begin < 0:
        begin += 5 * mn1
    if end < m - 5:
        end += 5
    counter += (end - begin) // 5 + 1
    if begin == 0:
        mn1 += 1
    begin -= 1
    end -= 1
print(counter)
