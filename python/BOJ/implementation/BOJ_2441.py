n = int(input())
for i in range(n, 0, -1):
    j = n - i
    print(' ' * j, end='')
    print('*' * i)