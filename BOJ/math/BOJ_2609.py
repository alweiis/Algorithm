def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1, num2 = map(int, input().split())
gcd = gcd(num1, num2)
lcm = (num1 * num2) // gcd
print(gcd)
print(lcm)