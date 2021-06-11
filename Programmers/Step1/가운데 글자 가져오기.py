def solution(s):
    index = len(s) // 2
    if len(s) % 2 == 0:
        return s[index - 1] +s[index]
    else:
        return s[index]