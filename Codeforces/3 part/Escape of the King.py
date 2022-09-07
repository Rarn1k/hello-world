def solution():
    """Алиса и Боб играют в шахматы на большом поле с размерами n×n. У Алисы осталась только одна фигура — ферзь,
    который находится в позиции (ax,ay), а у Боба остался только король, расположенный на (bx,by). Алиса считает, что
    поскольку её ферзь доминирует на поле, то победа уже её.

    Но Боб придумал хитрый план, который принесет ему победу, для этого ему нужно передвинуть его короля на позицию
    (cx,cy). Поскольку Алису отвлекает её чувство превосходства, она больше не передвигает её фигуру, поэтому только Боб
    может передвигать его фигуру.

    Боб победит, если он может передвинуть его короля с позиции (bx,by) на (cx,cy), не попадая под шах. Не забудьте, что
    король может передвигаться только в соседние 8 ячеек. Король находится под шахом, если находится в той же строке,
    столбце или диагонали, что и ферзь.

    Определите, сможет ли Боб победить или нет.

    Входные данные
    Первая строка содержит одно целое число n (3≤n≤1000) — размеры шахматного поля.

    Вторая строка содержит два целых числа ax и ay (1≤ax,ay≤n) — координаты ферзя Алисы.

    Третья строка содержит два целых числа bx и by (1≤bx,by≤n) — координаты короля Боба.

    Четвёртая строка содержит два целых числа cx и cy (1≤cx,cy≤n) — координаты позиции, куда Боб хочет передвинуть его
    короля.

    Гарантируется, что король Боба не находится под шахом и то, что конечная точка тоже не под шахом.

    Кроме того, король не находится на том же квадрате, что и ферзь (то есть ax≠bx или ay≠by), и конечная точка не
    совпадает ни с позицией ферзя (то есть cx≠ax или cy≠ay), ни с позицией короля (то есть cx≠bx или cy≠by).

    Выходные данные
    Выведите «YES» (без кавычек), если Боб может попасть из позиции (bx,by) в (cx,cy), не попадая под шах, иначе
    выведите «NO»."""
    n = int(input())
    queen_x, queen_y = [int(_) for _ in input().split()]
    king_x, king_y = [int(_) for _ in input().split()]
    escape_x, escape_y = [int(_) for _ in input().split()]
    if not (king_x < queen_x and escape_x < queen_x and (
            king_y < queen_y and escape_y < queen_y or king_y > queen_y and escape_y > queen_y)
            or king_x > queen_x and escape_x > queen_x and (
            king_y < queen_y and escape_y < queen_y or king_y > queen_y and escape_y > queen_y)):
        return False
    return True
    pass


if solution():
    print('YES')
else:
    print('NO')
