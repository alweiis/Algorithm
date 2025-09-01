name_list = [input() for _ in range(int(input()))]
asc_list = sorted(name_list)
desc_list = sorted(name_list, reverse=True)
if name_list == asc_list:
    print('INCREASING')
elif name_list == desc_list:
    print('DECREASING')
else:
    print('NEITHER')