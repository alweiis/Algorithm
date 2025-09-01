from collections import defaultdict
from sys import stdin
input = stdin.readline
n = int(input())
check = defaultdict(int)
for _ in range(2*n - 1):
    name = input().rstrip()
    check[name] += 1
for name, count in check.items():
    if count % 2 != 0:
        print(name)