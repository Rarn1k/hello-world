n = int(input())
a = int(input())
b = int(input())
x, y = 0, 0
for i in range(0, n + 1):
    if n - a * i >= 0 and (n - a * i) % b == 0:
        x = i
        y = (n - a * i) // b
        break

if x >= 0 and y > 0 or x > 0 and y >= 0:
    print("YES")
    print(x, y, sep=' ')
else:
    print("NO")
