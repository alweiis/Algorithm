def solution(s):
    stack = [s[0]]
    for c in s[1:]:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return 1 if len(stack) == 0 else 0