n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))
for j in range(1, n):
    print(' ' * j, end='')
    print('*' * ((n - j) * 2 - 1))