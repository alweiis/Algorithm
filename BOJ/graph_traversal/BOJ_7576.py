from sys import stdin
from collections import deque
input = stdin.readline

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque([])
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))
answer = -1
for i in range(N):
    if grid[i].count(0) > 0:
        answer = 0
        break
    else:
        answer = max(answer, max(grid[i]))
print(answer - 1)