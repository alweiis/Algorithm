formula = input()
stack = []
chemical = {'H': 1, 'C': 12, 'O': 16}
for c in formula:
    if c == '(':
        stack.append(c)
    elif c == ')':
        result = 0
        while stack:
            temp = stack.pop()
            if temp == '(':
                break
            result += temp
        stack.append(result)
    elif c in ['H', 'C', 'O']:
        stack.append(chemical[c])
    else:
        stack.append(stack.pop() * int(c))
print(sum(stack))