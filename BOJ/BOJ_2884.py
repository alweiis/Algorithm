h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    if h == 0:
        h = 24
    print(h-1, m+60-45)