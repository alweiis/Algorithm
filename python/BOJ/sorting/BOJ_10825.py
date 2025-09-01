from sys import stdin
n = int(stdin.readline())
init_lst = []
for _ in range(n):
    name, kor, math, eng = stdin.readline().split()
    init_lst.append((name, int(kor), int(math), int(eng)))
sorted_lst = sorted(init_lst, key=lambda x:(-x[1], x[2], -x[3], x[0]))
for item in sorted_lst:
    print(item[0])