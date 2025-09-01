def solution(k, m, score):
    n = len(score)
    answer = 0
    if n % m == 0:  # 모든 사과를 포장 가능 O
        score.sort()
        for i in range(0, n, m):
            answer += min(score[i:i+m]) * m
    else:           # 모든 사과를 포장 가능 X
        score.sort(reverse=True)
        for i in range(m, n, m):
            answer += min(score[i-m:i]) * m
    return answer