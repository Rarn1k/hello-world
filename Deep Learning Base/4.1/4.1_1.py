def almost_double_factorial(n):
    """
    Вычисляет произведение всех нечётных натуральных чисел, не превосходящих n.
    :param n: натуральное (ноль -- натуральное) число n ⩽ 100.
    :return: вычисленное произведение.
    """
    m = 1
    if n == 0:
        return 1
    for i in range(n + 1):
        if i % 2 != 0:
            m *= i
    return m


print(almost_double_factorial(5))
