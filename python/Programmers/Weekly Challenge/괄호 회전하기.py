from collections import deque

def check(strings):
    stack = []
    for c in strings:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        else:
            if stack:
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(c)
                elif c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(c)
                elif c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(c)
            else:
                return False
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.append(s.popleft())
    return answer