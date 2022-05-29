from collections import deque
n, k = map(int, input().split())
deq = deque([i for i in range(1, n + 1)])
ans = []
while deq:
    deq.rotate(-(k - 1))
    ans.append(deq.popleft())
print('<', end='')
print(', '.join(map(str, ans)), end='')
print('>')