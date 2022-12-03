def solution(s):
    answer = 0
    x, y = '', ''
    for c in s:
        if x == '':
            x += c
        else:
            if c == x[0]:
                x += c
            else:
                y += c
            if len(x) == len(y):
                answer += 1
                x, y = '', ''
    if x != '':
        answer += 1
    return answer