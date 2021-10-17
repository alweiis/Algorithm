n, m, k = map(int, input().split())
team = 0
while n >= 2 and m >= 1 and n+m >= k+3:
    team += 1
    n -= 2
    m -= 1
print(team)