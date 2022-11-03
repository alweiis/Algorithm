sticks = input()
stack = []
answer = 0
for i in range(len(sticks)):
    if sticks[i] == '(':        # 여는 괄호
        stack.append('(')
    else:                       # 닫는 괄호
        if sticks[i-1] == '(':  # 이전 값이 '('인 경우
            stack.pop()
            answer += len(stack)
        else:                   # 이전 값이 ')'인 경우
            stack.pop()
            answer += 1
print(answer)