n = int(input())
for i in range(1, n + 1):
    j = 2 * i - 1
    k = n - i
    print(' ' * k, end='')
    print('*' * j)
