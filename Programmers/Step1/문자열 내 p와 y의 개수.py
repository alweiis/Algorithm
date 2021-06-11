def solution(s):
    answer = True
    word = s.lower()
    p_cnt = word.count('p')
    y_cnt = word.count('y')
    if p_cnt != y_cnt:
        answer = False
    return answer