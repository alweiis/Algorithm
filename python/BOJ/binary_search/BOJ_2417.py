n = int(input())
start, end = 0, int((2 ** 63) ** 0.5) + 1
ans = 0
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 >= n:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)