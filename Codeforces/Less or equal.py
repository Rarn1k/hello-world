n, k = [int(i) for i in input().split()]
subsequence = [int(i) for i in input().split()]
search = True
subsequence.sort()
if n != k and k != 0 and subsequence[k - 1] < subsequence[k]:
    print(subsequence[k - 1])
    search = False
if n == k:
    print(subsequence[k - 1])
    search = False
if k == 0 and subsequence[0] - 1 >= 1:
    print(subsequence[0] - 1)
    search = False
if search:
    print(-1)
