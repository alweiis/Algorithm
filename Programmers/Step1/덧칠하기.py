def solution(n, m, section):
    l, r, answer = 0, 0, 0
    while l < len(section):
        flag = False
        while r < len(section) and section[r] - section[l] < m:
            r += 1
            flag = True
        if flag:
            answer += 1
            l = r
    return answer