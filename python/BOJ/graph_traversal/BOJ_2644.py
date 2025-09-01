from collections import deque

def bfs(x, y):
    que = deque([x])
    visited[x] = True
    while que:
        v = que.popleft()
        if v == y:
            return result[v]
        for e in graph[v]:
            if not visited[e]:
                que.append(e)
                visited[e] = True
                result[e] = result[v] + 1
    return -1

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
print(bfs(x, y))