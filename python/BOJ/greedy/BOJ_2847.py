n = int(input())
scores = list(reversed([int(input()) for _ in range(n)]))
answer = 0
for i in range(1, n):
    while scores[i-1] <= scores[i]:
        scores[i] -= 1
        answer += 1
print(answer)