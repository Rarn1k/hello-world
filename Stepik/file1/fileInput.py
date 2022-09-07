digits = set('0123456789')
with open('dataset_3363_2 (1).txt') as inf:
    s = inf.readline().strip()
c = s[0]
answer = ''
multi = ''
first = True
for i in range(len(s)):
    if s[i] in digits:
        multi += s[i]
    else:
        if multi:
            answer += (c * int(multi))
        c = s[i]
        multi = ''
answer += (c * int(multi))
with open('output.txt', 'w') as out:
    out.write(answer)
