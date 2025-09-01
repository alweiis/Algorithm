s = input()
stack = []
cnt = 0
for ele in s:
    if ele == '(':
        stack.append(ele)
    else:
        if len(stack) == 0:
            cnt += 1
        else:
            stack.pop()
cnt += len(stack)
print(cnt)