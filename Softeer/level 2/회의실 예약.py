n, m = map(int, input().split())
rooms = {}
for _ in range(n):
    name = input()
    rooms[name] = [0] * 18 + [1]

for _ in range(m):
    name, start, end = input().split()
    start, end = int(start), int(end)
    for i in range(start, end):
        rooms[name][i] = 1

rooms = dict(sorted(rooms.items()))

for idx, name in enumerate(rooms):
    print(f'Room {name}:')
    times = []
    current = 1
    for i in range(9, 19):
        if current == 1 and rooms[name][i] == 0:
            start = i
            current = 0
        elif current == 0 and rooms[name][i] == 1:
            end = i
            current = 1
            times.append([start, end])
    if len(times) == 0:
        print('Not available')
    else:
        print(f'{len(times)} available:')
        for t in times:
            print(f'{t[0]:02d}-{t[1]}')
    if idx != n-1:
        print('-----')