def warm():
    """
    Ноябрь длится n дней (n около миллиона или чуть меньше) мы заранее знаем температуру всех дней ноября.
    Нужно сказать людям через сколько дней наступит день более теплый, чем текущий.
    :return: массив со значениями, равными числам, через сколько дней наступит день более теплый, чем текущий.
    9 7 4 4 4 8 5 5 5 6 0 0 0 1 0 -5 -4 -3 0 0 -1 -1 -2 -8 -7 -1 4 1 -1 1 1
    None,4,3,2,1,None,3,2,1,None,3,2,1,13,12,1,1,1,8,7,6,5,3,1,1,1,None,None,1,None,None
    """
    print("Enter the temperatures of the days ")
    entered = [int(_) for _ in input().split()]
    stack = []
    n = len(entered)
    for i in range(n - 1, -1, -1):
        if len(stack) != 0:
            while len(stack) != 0 and entered[i] >= stack[-1][0]:
                stack.pop()
        temp = entered[i]
        if len(stack) != 0:
            entered[i] = stack[-1][1] - i
        else:
            entered[i] = 'None'
        stack.append((temp, i))
    return entered

    # print("Enter the temperatures of the days ")
    # entered = [int(_) for _ in input().split()]
    # n = len(entered)
    # warmer = ['None' for _ in range(n)]
    # max_degree = entered[n - 1]
    # i_max_degree = n - 1
    # for i in range(n - 2, 0, -1):
    #     if entered[i] >= max_degree:
    #         max_degree = entered[i]
    #         i_max_degree = i
    #     else:
    #         warmer[i] = i_max_degree - i
    #     if entered[i] < entered[i + 1]:
    #         warmer[i] = 1
    # return warmer

    # print("Enter temperatures of days ")
    # entered = [int(_) for _ in input().split()]
    # n = len(entered)
    # numbered = []
    # warmed = []
    # for i in range(n):
    #     numbered.append((entered[i], i))
    #     warmed.append('None')
    # numbered.sort(reverse=True)
    # print(numbered)
    # for i in range(1, n):
    #     j = numbered[i][1]
    #     if numbered[i][1] < numbered[i - 1][1]:
    #         warmed[j] = numbered[i - 1][1] - numbered[i][1]
    # return warmed


print(*warm(), sep=',')
