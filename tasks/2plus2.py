import math


def two_plus_two():
    start = math.ceil(math.sqrt(10 ** 5))

    for i in range(start, 999):
        two = set([int(_) for _ in str(i)])
        if len(two) == 3:
            a = i * i
            b = [int(_) for _ in str(a)]
            four = set(b)
            if two.isdisjoint(four) and len(four) == 5 and len(b) == 6:
                if b[1] == b[5]:
                    print("Два: " + str(i))
                    print("Четыре: " + str(a))
                    break


two_plus_two()
