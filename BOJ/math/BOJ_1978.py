from math import sqrt
from sys import stdin
n = int(input())
nums = list(map(int, stdin.readline().split()))
prime_num_cnt = 0

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for num in nums:
    if is_prime_number(num):
        prime_num_cnt += 1
print(prime_num_cnt)