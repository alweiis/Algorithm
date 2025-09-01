def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    result = (a * b) // gcd(a, b)
    return result

def solution(arr):
    a = 1
    for b in arr:
        a = lcm(a, b)
    return a