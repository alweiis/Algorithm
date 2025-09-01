t = int(input())
for idx in range(1, t + 1):
    a, b = map(int, input().split())
    x, y = divmod(a, b)
    print('#{} {} {}'.format(idx, x, y))