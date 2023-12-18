t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            bugs = 0
            for k in range(i, i + m):
                for l in range(j, j + m):
                    bugs += arr[k][l]
            answer = max(answer, bugs)
    print(f'#{tc} {answer}')
