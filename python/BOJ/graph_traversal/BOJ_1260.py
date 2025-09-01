from collections import deque

def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for e in graph[v]:
        if not visited_dfs[e]:
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not visited_bfs[v]:
            visited_bfs[v] = True
            print(v, end=" ")
            for e in graph[v]:
                if not visited_bfs[e]:
                    q.append(e)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(1, m + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited_dfs = [False] * (n + 1)
dfs(v)
print()
visited_bfs = [False] * (n + 1)
bfs(v)
