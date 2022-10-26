def solution(dartResult):
    dartResult = dartResult.replace('10', 'X')
    bonus = {'S': 1, 'D': 2, 'T': 3}
    stack = []
    for c in dartResult:
        if c.isdigit() or c == 'X':
            stack.append(10 if c == 'X' else int(c))
        elif c in bonus:
            score = stack.pop()
            stack.append(score ** bonus[c])
        elif c == '*':
            score = stack.pop()
            if stack:
                stack[-1] *= 2
            stack.append(score * 2)
        elif c == '#':
            stack[-1] *= -1
    return sum(stack)