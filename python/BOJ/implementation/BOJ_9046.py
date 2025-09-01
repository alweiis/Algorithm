T = int(input())
for _ in range(T):
    chk = dict()
    words = input().replace(' ', '')
    for c in words:
        chk[c] = chk.get(c, 0) + 1
    chk_ = sorted(chk.items(), key=lambda x: x[1], reverse=True)
    if len(chk_) > 1 and chk_[0][1] == chk_[1][1]:
        print('?')
    else:
        print(chk_[0][0])