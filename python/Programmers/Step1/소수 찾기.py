def solution(n):
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    answer = [i for i in range(2, n + 1) if sieve[i]]
    return len(answer)