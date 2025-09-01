def solution(s, n):
    answer = ''
    lst = list(s)
    for i in lst:
        change_num = ord(i)
        # 입력값이 공백일 때
        if change_num == 32:
            answer += i
        # 입력값이 소문자와 대문자 범위를 벗어날 때
        elif 65 <= change_num <= 90 and change_num + n > 90 or change_num + n > 122:
            answer += chr(change_num + n - 26)
        else:
            answer += chr(change_num + n)
    return answer
