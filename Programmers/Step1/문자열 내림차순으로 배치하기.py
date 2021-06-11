def solution(s):
    result = ''
    answer = sorted(s, reverse=True)
    for i in answer:
        result += i
    return result