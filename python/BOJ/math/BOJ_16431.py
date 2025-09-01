b = tuple(map(int, input().split()))
d = tuple(map(int, input().split()))
j = tuple(map(int, input().split()))
dtime = abs(d[0] - j[0]) + abs(d[1] - j[1])
btime = sum(divmod(abs(b[0] - j[0]) + abs(b[1] - j[1]), 2))
if btime < dtime:
    print('bessie')
elif btime > dtime:
    print('daisy')
else:
    print('tie')