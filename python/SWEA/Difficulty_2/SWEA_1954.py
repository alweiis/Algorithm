t = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for test_case in range(1, t+1):
    print(f'#{test_case}')
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    x, y = 0, 0
    num, k = 1, 0
    grid[x][y] = num
    while num < n * n:
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] != 0:
            k = (k + 1) % 4
            continue
        x, y = nx, ny
        num += 1
        grid[x][y] = num
    for i in range(n):
        print(*grid[i])