input_list = list(map(int, input().split()))
asc_list = [1, 2, 3, 4, 5, 6, 7, 8]
desc_list = [8, 7, 6, 5, 4, 3, 2, 1]
if input_list == asc_list:
    print('ascending')
elif input_list == desc_list:
    print('descending')
else:
    print('mixed')