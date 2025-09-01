n = int(input())
prices = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
stack = []
for price in prices:
    stack.append(price)
    if len(stack) == 3:
        stack.sort()
        answer += stack[1] + stack[2]
        stack = []
if stack:
    answer += sum(stack)
print(answer)