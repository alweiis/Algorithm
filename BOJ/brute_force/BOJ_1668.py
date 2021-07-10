n = int(input())
init_lst = [int(input()) for _ in range(n)]
length = len(init_lst)
left_cnt, right_cnt = 1, 1
for idx in range(1, length):
    if max(init_lst[:idx]) < init_lst[idx]:
        left_cnt += 1
init_lst.reverse()
for idx in range(1, length):
    if max(init_lst[:idx]) < init_lst[idx]:
        right_cnt += 1
print(left_cnt)
print(right_cnt)