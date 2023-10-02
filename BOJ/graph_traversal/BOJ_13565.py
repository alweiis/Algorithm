from sys import stdin
from collections import deque
input = stdin.readline

def bfs(i, j):
    visited[i][j] = True
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if grid[nx][ny] == '0' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
M, N = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
for i in range(N):
    if grid[0][i] == '0' and not visited[0][i]:
        bfs(0, i)
answer = 'NO'
for i in range(N):
    if grid[M-1][i] == '0' and visited[M-1][i]:
        answer = 'YES'
print(answer)