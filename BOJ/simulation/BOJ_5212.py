r, c = map(int, input().split())
map = [list(input()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sink_location = []
for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            sea_cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if map[nx][ny] == '.':
                        sea_cnt += 1
                else:
                    sea_cnt += 1
            if sea_cnt >= 3:
                sink_location.append((i, j))

if sink_location:
    for x, y in sink_location:
        map[x][y] = '.'

x1, y1 = 0, c-1
x2, y2 = 0, 0
for i in range(r):
    if 'X' in map[i]:
        x1 = i
        break
for i in range(r-1, -1, -1):
    if 'X' in map[i]:
        x2 = i
        break
for i in range(x1, x2+1):
    for j in range(c):
        if map[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        print(map[i][j], end='')
    print()