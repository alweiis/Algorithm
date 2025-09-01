def solution(n):
    lst = list(str(n))
    lst.sort(reverse=True)
    answer = ''.join(lst)
    return int(answer)
