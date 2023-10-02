from sys import stdin
from collections import deque
input = stdin.readline

def bfs(i, j):
    result = 1
    visited[i][j] = True
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    result += 1
    return result


N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 1
for _ in range(K):
    x, y = map(int, input().rstrip().split())
    grid[x-1][y-1] = 1
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(i, j))
print(answer)