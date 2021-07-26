import math
from sys import stdin

a, b = map(int, stdin.readline().split())
if a < b:
    a, b = b, a
print('1' * math.gcd(a, b))