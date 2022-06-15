import heapq

def solution(N, road, K):
    distance = [float('inf')] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return len([num for num in distance if num <= K])