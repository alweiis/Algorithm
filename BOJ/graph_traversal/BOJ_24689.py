from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < N):
                if arr[nx][ny] > k and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
for k in range(101):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i, j)
                count += 1
    answer = max(answer, count)
print(answer)