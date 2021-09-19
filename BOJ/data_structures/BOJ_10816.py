from sys import stdin
n = int(input())
n_nums = list(map(int, stdin.readline().split()))
m = int(input())
m_nums = list(map(int, stdin.readline().split()))
n_dic = {}
count = []

for num in n_nums:
    if num in n_dic:
        n_dic[num] += 1
    else:
        n_dic[num] = 1

for num in m_nums:
    if num in n_dic.keys():
        count.append(n_dic.get(num))
    else:
        count.append(0)
print(' '.join(map(str, count)))