import sys
sys.setrecursionlimit(100000)

def DFS(x, y):
    global town_cnt
    visited[x][y] = True
    town_cnt += 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if town[nx][ny] and not visited[nx][ny]:
            DFS(nx, ny)


n = int(input())

town = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
town_lst = []

for i in range(n):
    for j in range(n):
        if town[i][j] and not visited[i][j]:
            town_cnt = 0
            DFS(i, j)
            town_lst.append(town_cnt)

town_lst.sort()
print(len(town_lst))
for town_cnt in town_lst:
    print(town_cnt)