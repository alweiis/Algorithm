import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

chk = []
for i in range(1, N+1):
    count = 0
    visited = [False] * (N + 1)
    bfs(graph, i, visited)
    chk.append((i, count))
chk.sort(key=lambda x: (-x[1]))

for i in range(len(chk)):
    if chk[i][1] == chk[0][1]:
        print(chk[i][0], end=' ')