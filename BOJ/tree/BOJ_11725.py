from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (n + 1)
answer = [0] * (n + 1)
visited[1] = True
q = deque([1])
while q:
    node = q.popleft()
    edge = tree[node]
    for next_node in edge:
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = True
            answer[next_node] = node
for i in range(2, n + 1):
    print(answer[i])