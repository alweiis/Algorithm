from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    _password = stdin.readline().rstrip()
    stack, tmp = [], []
    if '<' not in _password and '>' not in _password and '-' not in _password:
        print(_password)
    else:
        for c in _password:
            if c.isalpha() or c.isdecimal():
                stack.append(c)
            else:
                if c == '-' and stack:
                    stack.pop()
                elif c == '<' and stack:
                    tmp.append(stack.pop())
                elif c == '>' and tmp:
                    stack.append(tmp.pop())
        while tmp:
            stack.append(tmp.pop())
        print(''.join(stack))