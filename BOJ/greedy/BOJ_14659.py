n = int(input())
hills = list(map(int, input().split()))
ans = 0
cnt = 0
max_hill = 0
for hill in hills:
    if hill > max_hill:
        max_hill = hill
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)
