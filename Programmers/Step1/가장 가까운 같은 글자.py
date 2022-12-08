def solution(s):
    checker = {}
    answer = []
    for idx, c in enumerate(s):
        if c in checker:
            answer.append(idx - checker[c])
            checker[c] = idx
        else:
            answer.append(-1)
            checker[c] = idx
    return answer