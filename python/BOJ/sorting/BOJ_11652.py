from sys import stdin
n = int(stdin.readline().rstrip())
tmp_dic = {}
for _ in range(n):
    num = int(stdin.readline().rstrip())
    if num in tmp_dic:
        tmp_dic[num] += 1
    else:
        tmp_dic[num] = 1
max_val = max(tmp_dic.values())
tmp_lst = sorted([k for k, v in tmp_dic.items() if v == max_val])
print(tmp_lst[0])
