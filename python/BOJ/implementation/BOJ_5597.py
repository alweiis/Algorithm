init_lst = [0] * 31
length = len(init_lst)
for _ in range(28):
    submit_idx = int(input())
    init_lst[submit_idx] = 1
for idx in range(1, length):
    if init_lst[idx] == 0:
        print(idx)