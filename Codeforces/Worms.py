def solution():
    """"""
    n = int(input())
    a = [int(_) for _ in input().split()]
    m = int(input())
    q = [int(_) for _ in input().split()]
    number = 0
    answer = {}
    j = 0
    for i in range(n):
        number += a[i]
        answer[number] = i + 1
    for i in range(m):
        print(answer.get(q[i] + 1))
    pass


solution()
