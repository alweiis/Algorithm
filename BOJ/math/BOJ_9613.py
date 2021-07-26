from math import gcd
from sys import stdin
from itertools import combinations

t = int(stdin.readline())
for _ in range(t):
    gcd_sum = 0
    tmp_lst = list(map(int, stdin.readline().split()))
    del tmp_lst[0]
    combination_lst = list(combinations(tmp_lst, 2))
    for num1, num2 in combination_lst:
        gcd_sum += gcd(num1, num2)
    print(gcd_sum)