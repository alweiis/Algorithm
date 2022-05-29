n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = nums[i] + nums[j] + nums[k]
            if ans < tmp <= m:
                ans = tmp
print(ans)