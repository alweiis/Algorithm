chk_num = int(input())
num, i = 1, 0
num_lst = []
while True:
    num = num + (6 * i)
    i += 1
    num_lst.append(num)
    if chk_num <= num:
        print(num_lst.index(num) + 1)
        break
