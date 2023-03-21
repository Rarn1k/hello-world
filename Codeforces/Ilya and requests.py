s = input()
m = int(input())
counter = [0] * m
sums = [0] * len(s)
for i in range(len(s)):
    if s[i] == s[i - 1]:
        sums[i] = sums[i - 1] + 1
    else:
        sums[i] = sums[i - 1]

for i in range(m):
    l, r = [int(_) for _ in input().split()]
    print(sums[r - 1] - sums[l - 1])
