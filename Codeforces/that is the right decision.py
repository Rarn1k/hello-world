n = int(input())
m = input()
digits = list()
number = 0
while n:
    digits.append(n % 10)
    n //= 10
digits.sort()
for i in range(len(digits)):
    if digits[i] == 0:
        for j in range(i + 1, len(digits)):
            if digits[j] != 0:
                tmp = digits[i]
                digits[i] = digits[j]
                digits[j] = tmp
                break
    break
for i in range(len(digits)):
    number += digits[i] * 10 ** (len(digits) - 1 - i)
if str(number) == m:
    print('OK')
else:
    print('WRONG_ANSWER')
