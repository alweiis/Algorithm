from collections import deque

def bfs(x, y, maps):
    q = deque([(x, y)])
    visited[x][y] = True
    food = int(maps[x][y])
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < w and 0 <= ny < h:
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    food += int(maps[nx][ny])
    answer.append(food)

def solution(maps):
    global w, h, dx, dy, answer, visited
    answer = []
    w = len(maps)
    h = len((maps[0]))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            if maps[i][j] != 'X' and not visited[i][j]:
                bfs(i, j, maps)
    if not answer:
        answer.append(-1)
    return sorted(answer)