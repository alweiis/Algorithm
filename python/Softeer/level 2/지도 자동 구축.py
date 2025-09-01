n = int(input())
dp = [0] * 16
dp[0] = 2
for i in range(1, 16):
    dp[i] = dp[i-1] + (dp[i-1] - 1)
print(dp[n] ** 2)