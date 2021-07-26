import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm

n = int(sys.stdin.readline())
for _ in range(n):
    num1, num2 = map(int, input().split())
    print(lcm(num1, num2))