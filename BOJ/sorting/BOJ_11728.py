from sys import stdin
n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
a.extend(b)
a.sort()
for ele in a:
    print(ele, end=' ')