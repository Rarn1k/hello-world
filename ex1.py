def sale():
    """Дана база данных о продажах некоторого интернет-магазина.
    Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
    где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов),
    количество — количество приобретенных единиц товара.
    Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных
    им единиц каждого вида товаров. Список покупателей, а также список товаров для
    каждого покупателя нужно выводить в лексикографическом порядке."""
    dict_s = {}
    while True:
        try:
            s = input().split()
            if (s[0], s[1]) not in dict_s:
                dict_s[(s[0], s[1])] = int(s[2])
            else:
                dict_s[(s[0], s[1])] += int(s[2])
        except:
            s = list()
            for k in sorted(dict_s):
                if k[0] != s:
                    s = k[0]
                    print(s + ':')
                    print(k[1], dict_s[k])
                else:
                    print(k[1], dict_s[k])
            break


sale()
