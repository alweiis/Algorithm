def dp(num):
    cache = [0] * 1001
    cache[1] = 1
    cache[2] = 2

    for i in range(3, num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[num] % 10007

n = int(input())
print(dp(n))