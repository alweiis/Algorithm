def get_divisor(n):
    divisors = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i ** 2 != n:
                divisors.append(n // i)
    return len(divisors)

def solution(number, limit, power):
    arr = []
    for i in range(1, number + 1):
        arr.append(get_divisor(i))
    answer = 0
    for n in arr:
        if n > limit:
            answer += power
        else:
            answer += n
    return answer