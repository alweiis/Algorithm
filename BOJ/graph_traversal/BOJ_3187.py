from collections import deque

def bfs(i, j):
    visited[i][j] = True
    s, w = 0, 0
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        if array[x][y] == 'k':
            s += 1
        elif array[x][y] == 'v':
            w += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and array[nx][ny] != '#':
                    que.append((nx, ny))
                    visited[nx][ny] = True
    if s > w:
        return [s, 0]
    else:
        return [0, w]

r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sheep, wolf = 0, 0

for i in range(r):
    for j in range(c):
        if array[i][j] in ['v', 'k'] and not visited[i][j]:
            result = bfs(i, j)
            sheep += result[0]
            wolf += result[1]
print(sheep, wolf)