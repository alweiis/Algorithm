def solution(num):
    cnt = 0
    for i in range(1, num + 1):
        total = 0
        while total < num:
            total += i
            i += 1
        if total == num:
            cnt += 1
    return cnt
