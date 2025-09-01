def solution(n):
    zero_cnt = divide(n)
    while True:
        n += 1
        calc_cnt = divide(n)
        if zero_cnt == calc_cnt:
            break
    return n


def divide(x):
    cnt = 0
    while True:
        a, b = divmod(x, 2)
        x = a
        if b == 1:
            cnt += 1
        if a == 0:
            break
    return cnt