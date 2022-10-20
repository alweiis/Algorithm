def solution(a, b, n):
    answer = 0
    while n >= a:
        q, r = divmod(n, a)
        answer += q * b
        n = q * b + r
    return answer