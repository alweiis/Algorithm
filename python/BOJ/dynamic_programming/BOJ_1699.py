n = int(input())
m = int(n ** 0.5)
dp = [i for i in range(n+1)]
for i in range(2, m+1):
    for j in range(i * i, n+1):
        dp[j] = min(dp[j], dp[j-i*i] + 1)
print(dp[n])