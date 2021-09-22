from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    Queue = deque(map(int, stdin.readline().split()))
    tmp = deque([0] * N)
    tmp[M] = 1
    count = 0
    while Queue:
        num = Queue[0]
        if num < max(Queue):
            Queue.append(Queue.popleft())
            tmp.append(tmp.popleft())
        else:
            Queue.popleft()
            count += 1
            c = tmp.popleft()
            if c == 1:
                print(count)
                break