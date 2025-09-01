n = int(input())
for i in range(1, 2*n):
    if i <= n:
        print(' ' * (n - i), end='')
        print('*' * i)
    else:
        j = i % n
        print(' ' * j, end='')
        print('*' * (n - j))