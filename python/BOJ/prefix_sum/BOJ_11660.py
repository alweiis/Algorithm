from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
grid = []
for _ in range(n):
    numbers = list(map(int, input().split()))
    tmp_num = numbers[0]
    tmp_arr = [tmp_num]
    for i in range(1, n):
        tmp_num += numbers[i]
        tmp_arr.append(tmp_num)
    grid.append(tmp_arr)
new_grid = list(map(list, zip(*grid)))
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if y1 - 2 < 0:
        answer = sum(new_grid[y2-1][x1-1:x2])
    else:
        answer = sum(new_grid[y2-1][x1-1:x2]) - sum(new_grid[y1-2][x1-1:x2])
    print(answer)