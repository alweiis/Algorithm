import sys
from collections import defaultdict
input = sys.stdin.readline
s = input().rstrip()
q = int(input())
result = defaultdict(list)

for n in range(97, 122+1):
    tmp = []
    cnt = 0
    for j in range(len(s)):
        if s[j] == chr(n):
            cnt += 1
        tmp.append(cnt)
    result[chr(n)] = tmp

for _ in range(q):
    a, l, r = input().rstrip().split()
    l, r = int(l), int(r)
    if l > 0:
        print(str(result[a][r] - result[a][l-1]))
    else:
        print(str(result[a][r]))