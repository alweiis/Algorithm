import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    global order
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        traversal_order[v] = order
        order += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse=True)

visited = [False] * (N+1)
traversal_order = [0] * (N+1)
order = 1

bfs(graph, R, visited)
for i in range(1, len(traversal_order)):
    print(traversal_order[i])