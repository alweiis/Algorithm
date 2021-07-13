from sys import stdin
n = int(input())
num_lst = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
num_lst.sort()
for x, y in num_lst:
    print(x, y)