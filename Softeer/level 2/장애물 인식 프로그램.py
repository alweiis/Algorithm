import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    count = 0
    que = deque([(a, b)])
    maps[a][b] = 0
    while que:
        x, y = que.popleft()
        count += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                que.append((nx, ny))
                maps[nx][ny] = 0
    return count

n = int(input())
maps = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            answer.append(bfs(i, j))
answer.sort()
print(len(answer))
for block in answer:
    print(block)