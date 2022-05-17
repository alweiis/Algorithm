from sys import stdin
test_case = 0
while True:
    strings = stdin.readline().rstrip()
    test_case += 1
    if strings.count('-'):
        break
    stack = []
    for c in strings:
        if c == '{':
            stack.append(c)
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
    remain = ''.join(stack)
    operation_cnt = 0
    chk = ''
    for c in remain:
        chk += c
        if len(chk) == 2:
            if chk == '{{' or chk == '}}':
                operation_cnt += 1
            elif chk == '}{':
                operation_cnt += 2
            chk = ''
    print(f'{test_case}. {operation_cnt}')