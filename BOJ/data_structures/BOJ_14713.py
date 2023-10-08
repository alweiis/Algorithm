from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
S = [deque(input().rstrip().split()) for _ in range(n)]
L = deque(input().rstrip().split())

for _ in range(len(L)):
    for j in range(n):
        if L and S[j] and S[j][0] == L[0]:
            S[j].popleft()
            L.popleft()
            break

empty = True
for i in range(n):
    if S[i]:
        empty = False

if not L and empty:
    print('Possible')
else:
    print('Impossible')