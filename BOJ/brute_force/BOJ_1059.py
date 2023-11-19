l = int(input())
s = sorted(map(int, input().split()))
n = int(input())
idx, answer = 0, 0
for i in range(l):
    if s[i] > n:
        idx = i
        break
start = 1 if idx == 0 else s[idx - 1] + 1
for left in range(start, s[idx] - 1):
    for right in range(left + 1, s[idx]):
        if left <= n <= right:
            answer += 1
print(answer)