from sys import stdin
from collections import defaultdict
input = stdin.readline
n, m = map(int, input().split())
checker = defaultdict(int)
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        checker[word] += 1
sorted_list = sorted(checker.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
for word in sorted_list:
    print(word[0])