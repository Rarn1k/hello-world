import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as inf:
    l = inf.readline().strip()

r = requests.get(l)
r = link + r.text

flag = True
while flag:
    r = requests.get(r)
    if r.text.count('.txt'):
        print(r.text)
        r = link + r.text
    else:
        flag = False
        print(r.text)
