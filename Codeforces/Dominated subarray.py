for _ in range(int(input())):
    occ = 0
    n = int(input())
    length = n
    a = [int(_) for _ in input().split()]
    if len(a) < 2:
        print(-1)
    else:
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] == a[j] and j - i + 1 < length:
                    length = j - i + 1
        print(length)
