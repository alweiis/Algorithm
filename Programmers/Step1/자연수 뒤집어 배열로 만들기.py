def solution(n):
    answer = []
    for i in reversed(str(n)):
        answer.append(i)
    answer = list(map(int, answer))
    return answer