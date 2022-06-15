from collections import deque

def bfs():
    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K:
            print(path[x])
            break

        for dx in [x-1, x+1, 2*x]:
            if 0 <= dx <= 100000 and path[dx] == 0:
                queue.append(dx)
                path[dx] = path[x] + 1


N, K = map(int, input().split())
path = [0] * 100001
bfs()