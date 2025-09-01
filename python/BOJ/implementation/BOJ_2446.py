n = int(input())
for i in range(n - 1):
    print(' ' * i + '*' * (2*(n-i)-1))
print(' ' * (n-1) + '*')
for i in range(n - 2, -1, -1):
    print(' ' * i + '*' * (2*(n-i)-1))
