from sys import stdin

def chk_bal(item):
    stack = []
    for c in item:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
    if stack:
        return 'no'
    else:
        return 'yes'

while True:
    line = stdin.readline().rstrip('\n')
    if line == '.':
        break
    print(chk_bal(line))