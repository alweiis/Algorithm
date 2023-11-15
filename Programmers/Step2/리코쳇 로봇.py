from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    visited = [[-1] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    que = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                que.append((i, j))
                visited[i][j] = 0
    while que:
        x, y = que.popleft()
        if board[x][y] == 'G':
            return visited[x][y]
        for k in range(4):
            nx, ny = x, y
            while True:
                nx += dx[k]
                ny += dy[k]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'D':
                    nx -= dx[k]
                    ny -= dy[k]
                    break
                if nx < 0 or n <= nx or ny < 0 or m <= ny:
                    nx -= dx[k]
                    ny -= dy[k]
                    break
            if visited[nx][ny] == -1:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return -1