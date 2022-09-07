def cumsum_and_erase(A, erase=1):
    """
    сформировать массив B[0,…,N−1], где B_i = A_0 + ... + A_i-- массив частичных сумм массива A;
    удалить из массива B все элементы, равные параметру erase; получить массив C;
    вернуть C в качестве ответа
    :param A: массив A[0,…,N−1].
    :param erase: опциональный аргумент, по умолчанию равный 1.
    :return: массив С
    """
    B = []
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        B.append(sum)
    C = [i for i in B if i != erase]
    return C


print(cumsum_and_erase([5, 1, 4, 5, 14], 10))
