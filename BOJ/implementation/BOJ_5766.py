from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    checker = defaultdict(int)
    for _ in range(n):
        keys = list(map(int, input().split()))
        for key in keys:
            checker[key] += 1
    result = []
    for key, value in checker.items():
        result.append((key, value))
    result.sort(key=lambda x: x[1], reverse=True)   # value(포인트)를 기준으로 내림차순 정렬
    point = result[1][1]            # 2등 선수의 포인트
    answer = [result[1][0]]         # 2등 선수의 번호
    for i in range(2, len(result)):
        if result[i][1] == point:   # 2등 선수와 포인트가 동일하다면
            answer.append(result[i][0])
    answer.sort()
    print(*answer)