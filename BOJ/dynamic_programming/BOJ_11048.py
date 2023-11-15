n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = maze[0][0]
for x in range(n):
    for y in range(m):
        if 0 <= x + 1 < n and 0 <= y + 1 < m:
            dp[x+1][y+1] = max(dp[x+1][y+1], maze[x+1][y+1] + dp[x][y])
        if 0 <= x + 1 < n:
            dp[x+1][y] = max(dp[x+1][y], maze[x+1][y] + dp[x][y])
        if 0 <= y + 1 < m:
            dp[x][y+1] = max(dp[x][y+1], maze[x][y+1] + dp[x][y])
print(dp[n-1][m-1])