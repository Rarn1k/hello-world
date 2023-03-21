import math


def solution():
    """Маленькой Миле дали задачу. У неё есть n досок, пронумерованных целыми числами от 1 до n. Она должна покрасить их
     странным образом.

    Непокрашенная доска может быть покрашены в красный цвет, если её номер делится на число a, а также может быть
    покрашена в синий цвет, если её номер делится на число b. Таким образом, доска номер которой делится на a и на b
    может быть покрашена как в красный, так и в синий цвет.

    После покраски она получит p шоколадок за каждую доску красного цвета и q шоколадок за каждую доску синего цвета.

    Обратите внимание, что она может красить доски в любом порядке.

    Помогите Миле найти наибольшее количество шоколадок, которые она может получить.

    Входные данные
    Единственная строка содержит пять целых чисел n, a, b, p и q (1≤n,a,b,p,q≤10^9).

    Выходные данные
    Выведите одно целое число s — наибольшее количество шоколадок, которые может получить Мила."""
    n, a, b, red, blue = [int(_) for _ in input().split()]
    money = 0
    money += red * (n // a) + blue * (n // b)
    if red > blue:
        if a % b == 0 and b != 1:
            money -= blue * (n // a)
        elif b % a == 0 and a != 1:
            money -= blue * (n // b)
        elif math.gcd(a, b) != 1:
            money -= blue * (n // (a * b // math.gcd(a, b)))
        else:
            money -= blue * (n // (a * b))
    else:
        if b % a == 0 and a != 1:
            money -= red * (n // b)
        elif a % b == 0 and b != 1:
            money -= red * (n // a)
        elif math.gcd(a, b) != 1:
            money -= red * (n // (a * b // math.gcd(a, b)))
        else:
            money -= red * (n // (a * b))

    return money
    pass


print(solution())