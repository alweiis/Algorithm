bracket = input().replace('()', '2').replace('[]', '3')
flag = True
if bracket.count('(') != bracket.count(')'):
    flag = False
if bracket.count('[') != bracket.count(']'):
    flag = False
stack = []
left_bracket = ['(', '[']
if flag:
    for c in bracket:
        if c in left_bracket:
            stack.append(c)
        elif c.isdigit():
            stack.append(int(c))
        else:
            number = 0
            while stack and flag:
                temp = stack.pop()
                if temp not in left_bracket:
                    number += temp
                elif temp == '[':
                    if c == ')':
                        flag = False
                    elif c == ']':
                        number *= 3
                        break
                elif temp == '(':
                    if c == ']':
                        flag = False
                    elif c == ')':
                        number *= 2
                        break
            stack.append(number)
if flag:
    print(sum(stack))
else:
    print(0)