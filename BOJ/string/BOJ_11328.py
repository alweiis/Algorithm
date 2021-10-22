from sys import stdin
n = int(stdin.readline())
for _ in range(n):
    str1, str2 = stdin.readline().rstrip().split()
    lst1 = sorted(str1)
    lst2 = sorted(str2)
    print('Possible' if lst1 == lst2 else 'Impossible')