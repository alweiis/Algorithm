N, R, C = map(int, input().split())
answer = [['.'] * N for _ in range(N)]
check = (R + C) % 2
for i in range(N):
    for j in range(N):
        if check == (i + j) % 2:
            answer[i][j] = 'v'
for arr in answer:
    print(''.join(arr))