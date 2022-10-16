from itertools import combinations
def solution(number):
    answer = 0
    arr = list(combinations(number, 3))
    for element in arr:
        if sum(element) == 0:
            answer += 1
    return answer