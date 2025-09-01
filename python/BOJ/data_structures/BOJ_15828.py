from sys import stdin
from collections import deque
input = stdin.readline
buffer = deque([])
n = int(input())
while True:
    x = int(input())
    if x == -1:
        break
    if x != 0:
        if len(buffer) < n:
            buffer.append(x)
    else:
        buffer.popleft()
if buffer:
    print(*buffer)
else:
    print('empty')