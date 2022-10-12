import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
parts = sorted(map(int, input().split()))
start, end = 0, n - 1
answer = 0
while start < end:
    check = parts[start] + parts[end]
    if check == m:
        answer += 1
        start += 1
        end -= 1
    elif check < m:
        start += 1
    elif check > m:
        end -= 1
print(answer)