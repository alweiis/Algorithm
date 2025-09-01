num_lst = [int(input()) for _ in range(5)]
num_lst.sort()
print(sum(num_lst)//len(num_lst))
print(num_lst[2])