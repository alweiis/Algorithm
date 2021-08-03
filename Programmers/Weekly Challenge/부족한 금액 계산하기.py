def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += price * i
    answer = total - money
    if answer > 0:
        return abs(answer)
    return 0