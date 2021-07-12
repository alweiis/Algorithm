n = int(input())
row = 2 * n - 1
for i in range(1, row+1):
    if i <= n:
        print('*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i)
    else:
        j = i % n
        print('*' * (n - j) + ' ' * j + ' ' * j + '*' * (n - j))