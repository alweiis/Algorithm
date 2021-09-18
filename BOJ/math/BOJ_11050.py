from math import factorial
n, k = map(int, input().split())
result = int(factorial(n) / (factorial(k) * factorial(n - k)))
print(result)