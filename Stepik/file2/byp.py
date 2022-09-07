words = dict()
with open('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.lower()
        for word in line.split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
maximum = 1

for key, value in words.items():
    current = words[key]
    if current > maximum:
        maximum = current
        word_with_max_quantity = key

with open('output.txt', 'w') as out_f_obj:
    out_f_obj.write(word_with_max_quantity + ' ' + str(maximum))
