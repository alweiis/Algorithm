from math import floor

x, y = map(int, input().split())
fist_rate = floor((y * 100 / x))
if fist_rate >= 99:
    print(-1)
else:
    start, end = 1, x
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        nx, ny = x + mid, y + mid
        chk_rate = floor((ny * 100 / nx))
        if fist_rate < chk_rate:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    print(ans)