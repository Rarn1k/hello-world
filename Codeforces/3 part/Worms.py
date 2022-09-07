import bisect


def ceiling_key(d, key, keys):
    """Возвращает больший по значению, чем параметр, ближайший ключ в словаре"""
    if key in d:
        return d[key]
    idx = bisect.bisect_left(keys, key)
    idx += 1
    return idx


def solution():
    """Пора Кроту пообедать. Его друг Сурок приготовил вкусный обед.

    Сурок принес Кроту n упорядоченных кучек червей, таких, что в i-ой кучке содержатся ai червей. Он пронумеровал всех
    этих червей последовательными целыми числами: черви в первой кучке пронумерованы числами от 1 до a1, черви во второй
    кучке пронумерованы числами от a1+1 до a1+a2 и так далее. Смотрите пример для лучшего понимания.

    Крот не может съесть всех червей (Сурок принёс их слишком много для того, чтобы съесть за один подход). К тому же,
    насколько мы знаем, Крот слепой — поэтому Сурок помогает ему, называ номера самых сочных червей. Сурок даст Кроту
    червяка, только если Крот правильно назовет кучку, в которой лежит червяк.

    Крот просит вас ему помочь. Для всех сочных червей, которых назвал Сурок, подскажите Кроту правильные ответы.

    Входные данные
    В первой строке записано единственное целое число n (1≤n≤10^5), количество кучек.

    Во второй строке записано n целых чисел a1,a2,...,an (1≤ai≤10^3, a1+a2+...+an≤10^6), где ai — количество червей в
    i-й кучке.

    В третьей строке записано единственное целое число m (1≤m≤10^5), количество сочных червей, названных Сурком.

    В четвертой строке записано m целых чисел q1,q2,...,qm (1≤qi≤a1+a2+...+an) — номера сочных червей.

    Выходные данные
    Выведите m строк. В i-ой строке должно быть целое число — номер кучки, в которой лежит червяк под номером qi."""
    n = int(input())
    a = [int(_) for _ in input().split()]
    m = int(input())
    q = [int(_) for _ in input().split()]
    number = 0
    answer = {}
    for i in range(n):
        number += a[i]
        answer[number] = i + 1
    keys = sorted(answer.keys())
    for i in range(m):
        print(ceiling_key(answer, q[i], keys))
    pass


solution()
