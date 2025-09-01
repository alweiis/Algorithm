from sys import stdin as s
from collections import defaultdict
n = int(s.readline())
dic = defaultdict(list)
for _ in range(n):
    name, commute = s.readline().split()
    dic[name].append(commute)
ans = sorted([name for name in dic if len(dic[name]) % 2 == 1], reverse=True)
print('\n'.join(ans))