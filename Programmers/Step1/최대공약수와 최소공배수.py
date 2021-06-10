def solution(n, m):
    answer = []
    a, b = n, m

    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    answer.append(gcd)

    lcm = int(n / gcd) * int(m / gcd) * gcd
    answer.append(lcm)
    return answer