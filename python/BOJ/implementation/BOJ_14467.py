n = int(input())
chk_dic = {}
count = 0
for _ in range(n):
    # 소의 번호, 소의 위치
    a, b = map(int, input().split())
    if a in chk_dic.keys():
        if chk_dic[a] != b:
            chk_dic[a] = b
            count += 1
    else:
        chk_dic[a] = b
print(count)