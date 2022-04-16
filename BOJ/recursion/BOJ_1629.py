def power(a, n, b):
    if n == 0:
        return 1
    x = power(a, n // 2, b)
    if n % 2 == 0:
        return (x * x) % b
    else:
        return (x * x * a) % b

a, b, c = map(int, input().split())
print(power(a, b, c))
