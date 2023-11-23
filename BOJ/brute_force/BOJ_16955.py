def check(x, y):
    for k in range(8):
        cnt, empty = 1, 0
        nx, ny = x, y
        for _ in range(4):
            nx += d[k][0]
            ny += d[k][1]
            if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                continue
            if grid[nx][ny] == 'X':
                cnt += 1
            if grid[nx][ny] == '.':
                empty += 1
        if cnt == 4 and empty == 1:
            return True
    return False

grid = [list(input()) for _ in range(10)]
answer = 0
d =[(0, 1), (1, 1), (1,0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
start = []
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'X':
            start.append((i, j))
for a, b in start:
    if check(a, b):
        answer = 1
print(answer)