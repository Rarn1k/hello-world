def solution():
    """Как вам хорошо известно, в этом году самые модные числа — это так называемые треугольные числа (то есть целые
    числа, представимые в виде k*(k+1)/2, где k — некоторое целое положительное число), а самые крутые — те, которые
    представимы в виде суммы двух треугольных.

    Небезызвестный хипстер Андрей очень любит все модное и крутое, но, к сожалению, он не дружит с математикой. Помогите
     ему по числу n сказать, раскладывается ли оно в сумму двух треугольных чисел (не обязательно различных)!

    Входные данные
    В первой строке записано целое число n (1≤n≤10^9).

    Выходные данные
    Выведите «YES» (без кавычек), если n раскладывается в сумму двух треугольных, и «NO» (без кавычек) в противном
    случае."""
    n = int(input())
    trends = set()
    i = 1
    while i * (i + 1) / 2 <= n:
        trends.add(i * (i + 1) // 2)
        i += 1
    i = 1
    while i * (i + 1) // 2 <= n:
        x = n - (i * (i + 1) // 2)
        if x in trends:
            return "YES"
        i += 1
    return "NO"
    pass


print(solution())
