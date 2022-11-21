import sys
input = sys.stdin.readline

dp = [0] * 1000001
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for _ in range(int(input())):
    n = int(input())
    print(dp[n])