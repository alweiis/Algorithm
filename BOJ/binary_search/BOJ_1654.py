import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = sorted([int(input()) for _ in range(k)])
start, end = 1, arr[-1]
answer = []
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(len(arr)):
        count += arr[i] // mid
    if count >= n:
        start = mid + 1
        answer.append(mid)
    elif count < n:
        end = mid - 1
print(max(answer))