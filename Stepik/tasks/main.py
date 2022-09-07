class_rawinfo = {}
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
with open('dataset_3380_5 (2).txt') as in_f_obj:
    for line in in_f_obj:
        string = line.rstrip().split('\t')
        if string[0] not in class_rawinfo:
            class_rawinfo[string[0]] = [int(string[2]), 1]
        elif string[0] in class_rawinfo:
            heights = class_rawinfo[string[0]][0] + int(string[2])
            students = class_rawinfo[string[0]][1] + 1
            class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
    class_info[int(k) - 1] = v[0] / v[1]

with open('output.txt', 'w') as out_f_obj:
    for i in range(len(class_info)):
        output = str(i + 1) + ' ' + str(class_info[i]) + '\n'
        out_f_obj.write(output)
