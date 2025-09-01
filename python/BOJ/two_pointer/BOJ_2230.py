from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
answer = float('inf')
start, end = 0, 1
while start < n and end < n:
    tmp = abs(arr[end] - arr[start])
    if tmp == m:
        print(m)
        exit(0)
    if tmp < m:
        end += 1
        continue
    start += 1
    answer = min(answer, tmp)
print(answer)