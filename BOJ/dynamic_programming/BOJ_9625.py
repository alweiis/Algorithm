K = int(input())
dp = [[]] * (45 + 1)
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, 45 + 1):
    count_a = dp[i-1][0] + dp[i-2][0]
    count_b = dp[i-1][1] + dp[i-2][1]
    dp[i] = [count_a, count_b]
print(dp[K][0], dp[K][1])