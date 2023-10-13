n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, int(1e9)
h = 0
while start <= end:
    mid = (start + end) // 2
    result = 0
    for tree in trees:
        if tree > mid:
            result += tree - mid
    if result >= m:
        start = mid + 1
        h = mid
    else:
        end = mid - 1
print(h)