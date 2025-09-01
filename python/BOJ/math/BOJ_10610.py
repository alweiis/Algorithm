n = input()
chk = list(map(int, n))
if sum(chk) % 3 != 0 or n.count('0') < 1:
    print(-1)
else:
    chk.sort(reverse=True)
    print(''.join(map(str, chk)))