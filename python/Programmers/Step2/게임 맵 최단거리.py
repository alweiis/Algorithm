from collections import deque

def solution(maps):
    n = len(maps)       # 2차원 배열의 세로 길이
    m = len(maps[0])    # 2차원 배열의 가로 길이
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    answer = -1
    q = deque([(0, 0)])
    maps[0][0] = 1
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        if (x, y) == (n-1, m-1):
            return maps[x][y]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m):
                if maps[nx][ny] != 0 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return answer