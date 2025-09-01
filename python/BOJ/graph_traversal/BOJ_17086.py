from collections import deque

def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        if grid[x][y] == 1:
            return visited[x][y]
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
distance = 1
for x in range(n):
    for y in range(m):
        if grid[x][y] == 0:
            distance = max(distance, bfs(x, y))
print(distance)