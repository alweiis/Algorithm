dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
n = int(input())
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])