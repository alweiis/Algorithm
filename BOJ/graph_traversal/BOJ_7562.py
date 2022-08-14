from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        if (x, y) == (goal_x, goal_y):
            return chess_board[x][y]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny]:
                chess_board[nx][ny] = chess_board[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

d = [(1, 2), (2, 1), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

T = int(input())
for _ in range(T):
    N = int(input())
    chess_board = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    curr_x, curr_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    print(bfs(curr_x, curr_y))