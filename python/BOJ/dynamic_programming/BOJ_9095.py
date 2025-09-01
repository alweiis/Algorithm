T = int(input())
dp = [0] * (10 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 10 + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for _ in range(T):
    i = int(input())
    print(dp[i])