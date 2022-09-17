def solution():
    """ Амуга владеет отелем, представимым в виде длинного коридора с 10 комнатами, идущими подряд. Комнаты
    пронумерованы цифрами от 0 до 9 слева направо.

    В отель есть два входа: с левого конца коридора и с правого. Если гость заходит с левого конца коридора, то он будет
    расположен в ближайшей к левому входу свободной комнате. Аналогично, если гость заходит с правого конца коридора,
    то ему будет назначена ближайшая к правому входу свободная комната.

    Однажды Амуга потерял документ с указанием статуса занятости комнат. К счастью, у него безупречная память, и он
    помнит всё о своих гостях: когда гость пришёл в отель, с какой стороны он вошёл, и когда он покинул отель.
    Изначально все комнаты в отеле были свободными. Напишите программу, которая восстановит статус занятости комнат по
    событиям из памяти Амуга.

    Входные данные
    Первая строка содержит одно целое число n (1≤n≤10^5) — количество событий в памяти Амуга.

    Вторая строка содержит строку длины n, описывающую события, которые помнит Амуга, заданные в хронологическом
    порядке. Символы заданной строки могут быть следующими:

    «L»: новый гость зашёл в отель с левого конца коридора.
    «R»: новый гость зашёл в отель с правого конца коридора.
    «0», «1», ..., «9»: гость из комнаты x (0, 1, ..., 9 соответственно) покинул отель.
    Гарантируется, что в отеле имеется хотя бы одна свободная комната, когда появляется новый гость. Также
    гарантируется, что, если задано x (0, 1, ..., 9), то в комнате x находится гость. В начальный момент времени все
    комнаты свободны.

    Выходные данные
    В единственной строке выведите статус занятости комнат, начиная с комнаты 0 и заканчивая комнатой 9. Свободную
    комнату обозначайте как «0», а занятую — как «1». Символы выводите без пробелов.
    """
    n = int(input())
    inp = input()
    events = list(inp)
    employment = [0] * 10
    for el in events:
        if el == "L":
            j = 0
            while employment[j] == 1:
                j += 1
            employment[j] = 1
        elif el == "R":
            j = 9
            while employment[j] == 1:
                j -= 1
            employment[j] = 1
        else:
            employment[int(el)] = 0
    for el in employment:
        print(el, end='')
    pass


solution()