n = int(input())
stack = []
stack2 = []
brackets = input()
for i in range(n):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        if stack:
            stack.pop()
        else:
            stack2.append(brackets[i])
if not stack and not stack2 or len(stack) == 1 and len(stack2) == 1:
    print('YES')
else:
    print('NO')
