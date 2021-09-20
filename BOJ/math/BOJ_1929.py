def is_prime_num(m, n):
    chk_prime = [False, False] + [True] * (n - 1)
    x = int(n ** 0.5)
    for i in range(2, x + 1):
        if chk_prime[i]:
            for j in range(i + i, n + 1, i):
                chk_prime[j] = False
    return [i for i in range(m, n + 1) if chk_prime[i]]

M, N = map(int, input().split())
prime_arr = is_prime_num(M, N)
for prime in prime_arr:
    print(prime)