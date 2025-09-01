from sys import stdin
input = stdin.readline

n, m, b = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
time = int(1e9)
height = 0

for h in range(257):
    block = b
    tmp_time = 0
    for i in range(n):
        for j in range(m):
            curr_h = grid[i][j]
            if curr_h > h:
                block += curr_h - h
                tmp_time += 2 * (curr_h - h)
            elif curr_h < h:
                block -= h - curr_h
                tmp_time += h - curr_h
    if block < 0:
        continue
    if tmp_time <= time:
        time = tmp_time
        height = h
print(time, height)