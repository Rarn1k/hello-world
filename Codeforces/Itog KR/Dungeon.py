def solution():
    """Вы играете в новую компьютерную игру, в которой необходимо сражаться с монстрами. В очередном подземелье вы
    встретили трех монстров; у одного из них a очков здоровья, у второго b очков здоровья, а у третьего — c.

    Для убийства монстров у вас есть пушка, которая наносит 1 единицу урона выбранному монстру. При этом каждый 7-й
    (т. е. выстрелы с номерами 7, 14, 21 и т. д.) выстрел пушки усиленный и наносит 1 урона всем монстрам, а не только
    одному из них. Если текущее здоровье монстра равно 0, он не может быть целью обычного выстрела и не получает урона
    от усиленного выстрела.

    Вы хотите красиво пройти подземелье, а именно, убить всех монстров одним и тем же усиленным выстрелом (т. е. после
    очередного усиленного выстрела очки здоровья каждого из монстров должны впервые стать равными 0). Каждый выстрел
    должен попадать в монстра, т. е. вы не можете стрелять мимо цели.

    Входные данные
    Первая строка содержит одного целое число t (1≤t≤10^4) — количество наборов входных данных.

    Каждый набор входных данных состоит из единственной строки, которая содержит три целых числа a, b и c (1≤a,b,c≤10^8)
    — количество очков здоровья у каждого из монстров.

    Выходные данные
    Для каждого набора входных данных выведите YES, если можно убить всех монстров одним и тем же усиленным выстрелом.
    Иначе выведите NO."""
    t = int(input())
    for _ in range(t):
        a, b, c = [int(_) for _ in input().split()]
        kolvo = (a + b + c) // 9
        if (a + b + c) % 9 == 0 and a >= kolvo and b >= kolvo and c >= kolvo:
            print('YES')
        else:
            print('NO')
    pass


solution()
