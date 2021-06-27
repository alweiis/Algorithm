def solution(s):
    lst = list(map(int, s.split()))
    answer = '{} {}'.format(min(lst), max(lst))
    return answer