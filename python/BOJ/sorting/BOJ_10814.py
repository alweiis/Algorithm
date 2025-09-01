from sys import stdin
n = int(stdin.readline())
init_lst = []
for _ in range(n):
    age, name = tuple(stdin.readline().split())
    init_lst.append((int(age), name))
sorted_lst = sorted(init_lst, key=lambda x:(x[0]))
for age, name in sorted_lst:
    print(age, name)