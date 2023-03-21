s = input()
t = input()
sAr = [int(i) for i in s]
tAr = [int(i) for i in t]
p = []
switcher = True
k = 0
for i in range(len(sAr)):
    if sAr[i] != tAr[i]:
        if switcher:
            p.append(sAr[i])
            k = 1
            switcher = False
        else:
            p.append(tAr[i])
            k = 0
            switcher = True
    else:
        p.append(sAr[i])
if k == 0:
    print(*p, sep='')
else:
    print("impossible")
