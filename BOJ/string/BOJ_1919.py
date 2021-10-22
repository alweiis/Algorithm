from sys import stdin
str1, str2 = stdin.readline().rstrip(), stdin.readline().rstrip()
dic1, dic2 = {}, {}
str1_len, str2_len = len(str1), len(str2)
common_num = 0
for alpha in str1:
    if alpha in dic1:
        dic1[alpha] += 1
    else:
        dic1[alpha] = 1

for alpha in str2:
    if alpha in dic2:
        dic2[alpha] += 1
    else:
        dic2[alpha] = 1

for key in dic1.keys():
    if key in dic2:
        str1_cnt, str2_cnt = dic1[key], dic2[key]
        common_num += str1_cnt if str1_cnt <= str2_cnt else str2_cnt

remove_num = (str1_len - common_num) + (str2_len - common_num)
print(remove_num)