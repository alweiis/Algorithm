n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = []
for i in range(n - 7):
    for j in range(m - 7):
        w_count, b_count = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        w_count += 1
                    if board[a][b] != 'B':
                        b_count += 1
                else:
                    if board[a][b] != 'B':
                        w_count += 1
                    if board[a][b] != 'W':
                        b_count += 1
        answer.append(w_count)
        answer.append(b_count)
print(min(answer))