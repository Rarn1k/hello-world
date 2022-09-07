for _ in range(int(input())):
    number_of_parcels = int(input())
    coordinates = list(())
    way = list()
    mistake = True

    for _ in range(number_of_parcels):
        x, y = [int(_) for _ in input().split()]
        coordinates.append((x, y))

    coordinates.sort()

    x_last, y_last = 0, 0

    for i in range(number_of_parcels):
        r = coordinates[i][0] - x_last
        u = coordinates[i][1] - y_last
        x_last = coordinates[i][0]
        y_last = coordinates[i][1]
        if r < 0 or u < 0:
            print('NO')
            mistake = False
            break
        way.append('R' * r + 'U' * u)

    if mistake:
        print('YES')
        print(''.join(way))
