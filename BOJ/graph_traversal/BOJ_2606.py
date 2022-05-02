def DFS(v):
    infected[v] = True
    for i in network[v]:
        if not infected[i]:
            DFS(i)

n, m = int(input()), int(input())
network = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)
infected = [False] * (n + 1)
DFS(1)
print(infected[2:].count(True))