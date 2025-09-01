from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y):
    que = deque([(x, y)])
    grid[x][y] = 0
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    grid[nx][ny] = grid[x][y] + 1
                    visited[nx][ny] = True

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
start_x, start_y = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_x, start_y = i, j
bfs(start_x, start_y)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            grid[i][j] = -1
for row in grid:
    for i in row:
        print(i, end=' ')
    print()