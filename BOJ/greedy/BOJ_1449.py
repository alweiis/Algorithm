N, L = map(int, input().split())
locations = sorted(map(int, input().split()))
start = locations[0]
answer = 0
for i in range(1, N):
    check = locations[i] - start
    if check >= L:
        start = locations[i]
        answer += 1
answer += 1
print(answer)