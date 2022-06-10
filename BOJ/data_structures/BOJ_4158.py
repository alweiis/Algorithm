import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    count = 0
    if N == 0 and M == 0:
        break
    cd = defaultdict(int)
    for _ in range(N):
        num = int(input())
        cd[num] = 1
    for _ in range(M):
        num = int(input())
        if cd.get(num) == 1:
            count += 1
    print(count)