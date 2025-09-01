import sys
input = sys.stdin.readline

N = int(input())
grade = [int(input()) for _ in range(N)]
grade.sort()
ans = 0
for i in range(1, N+1):
    ans += abs(i - grade[i-1])
print(ans)