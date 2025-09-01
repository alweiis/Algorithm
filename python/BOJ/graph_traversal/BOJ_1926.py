from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y, painting):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        painting +=1
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if paper[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    area.append(painting)

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 0
area = [0]

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            bfs(i, j, 0)
            count += 1
print(count)
print(max(area))