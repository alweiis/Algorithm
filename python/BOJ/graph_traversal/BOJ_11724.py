import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def DFS(x):
    visited[x] = True
    for e in graph[x]:
        if not visited[e]:
            DFS(e)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

connected_comp = 0
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        connected_comp += 1
print(connected_comp)