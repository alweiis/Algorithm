from math import gcd
n, m = map(int, input().split(':'))
gcd = gcd(n, m)
print(f'{n // gcd}:{m // gcd}')