n, m = map(int, input().split())
chk = [0] * m
x_guard = 0
for _ in range(n):
    floor = input()
    for i in range(m):
        if floor[i] == 'X':
            chk[i] = 1
    if 'X' not in floor:
        x_guard += 1
y_guard = chk.count(0)
print(max(x_guard, y_guard))