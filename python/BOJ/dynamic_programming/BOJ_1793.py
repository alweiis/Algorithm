def dp(num):
    dp = [1] * (250 + 1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    dp[4] = 11

    for i in range(5, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2
    return dp[num]

while True:
    try:
        n = int(input())
        print(dp(n))
    except:
        exit()
