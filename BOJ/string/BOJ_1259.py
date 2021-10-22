while True:
    init_lst = list(map(int, input()))
    if init_lst == [0]:
        break
    chg_lst = init_lst.copy()
    chg_lst.reverse()
    print('yes' if init_lst == chg_lst else 'no')