from collections import deque

def BFS(x, y):
    q = deque([(x, y)])
    farm[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (0 <= nx < M) and (0 <= ny < N) and farm[nx][ny] == 1:
                q.append((nx, ny))
                farm[nx][ny] = 0

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    bug = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                BFS(i, j)
                bug += 1
    print(bug)