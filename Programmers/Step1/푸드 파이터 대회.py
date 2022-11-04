def solution(food):
    answer = ''
    for i in range(1, len(food)):
        n = food[i] // 2
        answer += str(i) * n
    answer = answer + '0' + answer[::-1]
    return answer