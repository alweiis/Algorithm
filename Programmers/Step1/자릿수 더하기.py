def solution(n):
    answer = 0
    num = str(n)
    for i in range(len(num)):
        answer += int(num[i])
    return answer