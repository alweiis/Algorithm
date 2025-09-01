from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    scores = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
    scores.sort(key=lambda x: x[0])
    top = 0
    count = 1
    for i in range(1, n):
        if scores[i][1] < scores[top][1]:
            top = i
            count += 1
    print(count)