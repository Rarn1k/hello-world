s = input()
stack = []
counter = 0
pos = True
for i in range(len(s)):
    if s[i] == '(' or s[i] == '<' or s[i] == '{' or s[i] == '[':
        stack.append(s[i])
    else:
        if stack and (s[i] == ')' and stack[len(stack) - 1] == '(' or s[i] == '>' and stack[len(stack) - 1] == '<' or
                      s[i] == '}' and stack[len(stack) - 1] == '{' or s[i] == ']' and stack[len(stack) - 1] == '['):
            stack.pop()
        else:
            if stack:
                stack.pop()
                counter += 1
            else:
                pos = False
                break
if not stack and pos:
    print(counter)
else:
    print('Impossible')
