N = int(input())
towers = list(map(int, input().split()))
stack, answer = [[towers[0], 1]], [0]
for idx, h in enumerate(towers[1:], start=2):
    while stack:
        if stack[-1][0] > h:
            answer.append(stack[-1][1])
            stack.append([h, idx])
            break
        elif stack[-1][0] < h:
            stack.pop()
    else:
        stack.append([h, idx])
        answer.append(0)
for a in answer:
    print(a, end=' ')