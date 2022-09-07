number_of_cases = int(input())
for _ in range(number_of_cases):
    number_of_groups = 0
    in_one_group = 0
    number_of_trackers = int(input())
    inexperience = [int(_) for _ in input().split()]
    inexperience.sort()
    for i in range(number_of_trackers):
        if in_one_group < inexperience[i]:
            in_one_group += 1
        if in_one_group == inexperience[i]:
            number_of_groups += 1
            in_one_group = 0
    print(number_of_groups)
