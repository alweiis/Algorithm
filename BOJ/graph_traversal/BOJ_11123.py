from collections import deque

def bfs(i, j):
    visited[i][j] = 1
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] == '#' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    answer = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#' and visited[i][j] == 0:
                answer += 1
                bfs(i, j)
    print(answer)