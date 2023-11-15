a, k = map(int, input().split())
dp = [0] * (k + 1)
for i in range(a, k):
    if i + 1 <= k and dp[i+1] == 0:
        dp[i+1] = dp[i] + 1
    if i * 2 <= k and dp[i*2] == 0:
        dp[i*2] = dp[i] + 1
print(dp[k])