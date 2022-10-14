from collections import deque
n = int(input())
arr = deque(range(1, n + 1))
step = list(map(int, input().split()))
step.reverse()
answer = deque()
for i in step:
    if i == 1:
        answer.appendleft(arr.popleft())
    elif i == 2:
        answer.insert(1, arr.popleft())
    elif i == 3:
        answer.append(arr.popleft())
print(*answer)