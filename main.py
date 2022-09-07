n, k, m = map(int, input().split())
A = map(int, input().split())

C = [0] * m

for a in A:
    C[a % m] += 1

for i in range(m):
    if C[i] >= k:
        break
else:
    print('No')
    exit()

print('Yes')
for a in A:
    if a % m == i:
        print(a),
        k -= 1
        if k == 0:
            break
print('')
