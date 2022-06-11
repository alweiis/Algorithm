import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
B = sorted([int(input()) for _ in range(N)])
chk = defaultdict(list)
for idx, num in enumerate(B):
    chk[num].append(idx)
for _ in range(M):
    num = int(input())
    if num in chk:
        print(chk[num][0])
    else:
        print(-1)