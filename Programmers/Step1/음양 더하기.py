def solution(absolutes, signs):
    answer = 0
    for idx in range(len(signs)):
        if signs[idx]:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
    return answer