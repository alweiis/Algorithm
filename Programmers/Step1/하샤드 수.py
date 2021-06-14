def solution(x):
    answer = True
    str_x = str(x)
    num = 0
    for i in range(len(str_x)):
        num += int(str_x[i])
    if x % num != 0:
        answer = False
    return answer