def solution(t, p):
    answer = 0
    x = len(t) - len(p)
    for i in range(x + 1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer