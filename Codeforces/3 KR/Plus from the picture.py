def solution():
    """Вам дан рисунок с размерами w×h. Определите, имеет ли данный рисунок одну «+» форму или нет. «+» форма определена
     ниже:

    «+» форма имеет одну центральную заполненную клетку.
    Должно быть несколько (как минимум одна) последовательных заполненных клеток в каждом направлении (влево, вправо,
    вверх, вниз) от центра, то есть каждый из четырёх лучей должен быть непустым.
    Все остальные клетки незаполненны.
    Определите, имеет ли данный рисунок одну «+» форму или нет.

    Входные данные
    Первая строка содержит два целых числа h и w (1≤h, w≤500) — высота и длина рисунка.

    i-я из следующих h строк содержит строку si длины w, которая состоит из «.» и «*», где «.» обозначает незаполненную
    клетку, а «*» обозначает заполненную клетку.

    Выходные данные
    Если данное изображение удовлетворяет всем условиям, выведите «YES». Иначе выведите «NO»."""
    h, w = [int(_) for _ in input().split()]
    picture = []
    [[picture.append(_) for _ in input().split()] for _ in range(h)]
    first_j, first_i = True, True
    start_i, start_j, last_i, last_j = -1, -1, h, w
    for i in range(h):
        picture[i] += '.'
    picture.append('.')
    for i in range(w):
        picture[h] += '.'
    if h == 1 and w == 1:
        return 'NO'
    for i in range(h):
        for j in range(w):
            if (first_j or first_i) and picture[i][j] == '*':
                if picture[i + 1][j] == '*' and first_j:
                    start_j = j
                    first_j = False
                elif not first_j and picture[i + 1][j] == '*' and j == start_j:
                    start_j = j
                elif picture[i][j + 1] == '*' and picture[i][start_j] == '*' and picture[i][start_j + 1] == '*':
                    start_i = i
                    first_i = False
                else:
                    return 'NO'
            if picture[i][j] == '*' and not first_j and not first_i:
                if i != start_i and j != start_j:
                    return 'NO'
                if j == start_j and i > last_i or i == start_i and j > last_j:
                    return 'NO'
            if not first_j and picture[i - 1][start_j] == '*' and picture[i][start_j] != '*' and i >= start_i:
                last_i = i
            if not first_i and picture[start_i][j - 1] == '*' and picture[start_i][j] != '*' and j >= start_j:
                last_j = j
    if picture[start_i + 1][start_j] == '*':
        return 'YES'
    else:
        return 'NO'
    pass


print(solution())
