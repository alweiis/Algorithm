def solution(s):
    answer = True
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in s:
        if i not in num_list or len(s) != (4 or 6):
            answer = False
            break
    return answer