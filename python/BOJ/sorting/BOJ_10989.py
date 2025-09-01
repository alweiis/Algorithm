from sys import stdin
n = int(stdin.readline())
num_lst = [0] * 10001
for _ in range(n):
    input_num = int(stdin.readline())
    num_lst[input_num] += 1

for idx in range(1, 10000 + 1):
    if num_lst[idx] != 0:
        for _ in range(num_lst[idx]):
            print(idx)