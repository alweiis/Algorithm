from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
answer = set()
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
if graph[1]:
    for first in graph[1]:
        answer.add(first)
    temp = list(answer)
    for num in temp:
        for second in graph[num]:
            answer.add(second)
if answer:
    answer.remove(1)
print(len(answer))