from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    score = deque(sorted([int(input()) for _ in range(n)]))
    idx = round(n * 0.15 + 0.0000001)
    for _ in range(idx):
        score.popleft()
        score.pop()
    score_sum = sum(score)
    score_len = len(score)
    print(round(score_sum / score_len + 0.0000001))