sound = list(input())
n = len(sound)
visited = [False] * n
duck = ['q', 'u', 'a', 'c', 'k']
answer = 0

for i in range(n):
    if visited[i]:
        continue
    idx = 0
    check = False
    for j in range(i, n):
        if visited[j]:
            continue
        if sound[j] == duck[idx]:
            visited[j] = True
            idx += 1
            if idx == 5:
                check = True
                idx = 0
    if check:
        answer += 1
    if idx or not visited[i]:
        print(-1)
        exit()
print(answer)
