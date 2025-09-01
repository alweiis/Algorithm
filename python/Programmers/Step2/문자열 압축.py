def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp_str = ''
        cnt = 1
        for x in range(0, len(s) + 1, i):
            temp = s[x:x+i]
            if comp_str == temp:
                cnt += 1
            elif comp_str != temp:
                comp_len += len(temp)
                if cnt > 1:
                    comp_len += len(str(cnt))
                cnt = 1
                comp_str = temp
        answer = min(answer, comp_len)
    return answer