import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    list_a = sorted(map(int, input().split()))
    list_b = sorted(map(int, input().split()))
    count = 0
    for a in list_a:
        start, end = 0, m - 1
        while start <= end:
            mid = (start + end) // 2
            if a > list_b[mid]:
                start = mid + 1
            else:
                end = mid - 1
        count += (end + 1)
    print(count)