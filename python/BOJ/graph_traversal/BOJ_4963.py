import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    visited[y][x] = True
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if (0 <= nx < w) and (0 <= ny < h):
            if not visited[ny][nx] and island_map[ny][nx] == 1:
                dfs(nx, ny)

d = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
while True:
    w, h = map(int, input().split())
    if h == 0:
        break
    island_map = []
    for _ in range(h):
        island_map.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]
    island_cnt = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and island_map[y][x] == 1:
                dfs(x, y)
                island_cnt += 1
    print(island_cnt)