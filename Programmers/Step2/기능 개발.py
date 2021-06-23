def solution(progresses, speeds):
    answer = []
    while progresses:
        for idx in range(len(progresses)):
            progresses[idx] += speeds[idx]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer

