from collections import deque

def bfs(a, b, c):
    que = deque([[a, b, c]])
    while que:
        x, y, nums = que.popleft()
        if len(nums) < 6:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    que.append([nx, ny, nums + grid[nx][ny]])
        elif len(nums) == 6:
            answer.add(nums)

grid = [input().split() for _ in range(5)]
answer = set()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(5):
    for j in range(5):
        bfs(i, j, grid[i][j])
print(len(answer))