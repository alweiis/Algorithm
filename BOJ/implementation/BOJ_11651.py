from sys import stdin
n = int(stdin.readline())
int_lst = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
sorted_lst = sorted(int_lst, key=lambda x:(x[1], x[0]))
for x, y in sorted_lst:
    print(x, y)