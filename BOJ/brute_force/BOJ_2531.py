from collections import deque
from itertools import islice
from sys import stdin
input = stdin.readline

deq = deque()
N, d, k, c = map(int, input().split())
answer = 0
for _ in range(N):
    deq.append(int(input()))

for _ in range(N):
    dishes = set(islice(deq, k))
    cnt = len(dishes)
    if c not in dishes:
        cnt += 1
    answer = max(answer, cnt)
    deq.rotate(-1)
print(answer)