num_lst = list()
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        num_lst.pop()
    else:
        num_lst.append(num)
print(sum(num_lst))