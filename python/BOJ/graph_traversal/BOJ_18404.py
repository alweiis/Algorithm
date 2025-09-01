from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]
answer = []
d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

q = deque([(x, y)])
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if (1 <= nx <= n) and (1 <= ny <= n) and board[nx][ny] == 0:
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

for _ in range(m):
    a, b = map(int, input().split())
    answer.append(board[a][b])
print(*answer)