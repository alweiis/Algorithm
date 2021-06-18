def solution(L, x):
    if x not in L:
        return [-1]
    answer = [idx for idx, val in enumerate(L) if x == val]
    return answer