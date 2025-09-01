import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global order
    visited[v] = True
    traversal_order[v] = order
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()

visited = [False] * (N+1)
traversal_order = [0] * (N+1)
order = 1

dfs(graph, R, visited)
for i in range(1, len(traversal_order)):
    print(traversal_order[i])