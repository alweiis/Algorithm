from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    array[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and array[nx][ny] == 1:
                q.append((nx, ny))
                array[nx][ny] = array[x][y] + 1


n, m = map(int, input().split())
array = [list(map(int, input().rstrip())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bfs(0, 0)
print(array[n-1][m-1] + 1)