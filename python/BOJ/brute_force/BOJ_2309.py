from itertools import combinations

init_lst = [int(input()) for _ in range(9)]
com_lst = list(combinations(init_lst, 7))
anw_lst = []
for lst in com_lst:
    if sum(lst) == 100:
        anw_lst = sorted(lst)
        break
for val in anw_lst:
    print(val)