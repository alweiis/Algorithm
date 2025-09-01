from sys import stdin
for _ in range(int(input())):
    n = int(input())
    n_list = stdin.readline().split()
    n_dic = {num: 1 for num in n_list}
    m = int(input())
    m_list = stdin.readline().split()
    for num in m_list:
        if n_dic.get(num):
            print(1)
        else:
            print(0)