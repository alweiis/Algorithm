n = int(input())
dp = [0] * 36
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-1-j]
print(dp[n])