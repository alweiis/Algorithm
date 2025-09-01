import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k, t, m = map(int, input().rstrip().split())
    record = {x:[0, 0, 0] for x in range(1, n + 1)}     # [최종점수, 제출횟수, 제출시간]
    score = {x:[0] * (k + 1) for x in range(1, n + 1)}
    for time in range(1, m + 1):
        i, j, s = map(int, input().rstrip().split())    # 팀 ID, 문제번호, 점수
        if score[i][j] < s:
            score[i][j] = s
            record[i][0] = sum(score[i])
        record[i][1] += 1
        record[i][2] = time
    results = list(record.items())
    results.sort(key = lambda x: (-x[1][0], x[1][1], x[1][2]))
    for i in range(len(results)):
        if results[i][0] == t:
            print(i + 1)