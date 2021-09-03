def solution(num):
    result = ''
    while num > 0:
        num, mod = divmod(num, 3)
        result += str(mod)
    answer = int(result, 3)
    return answer