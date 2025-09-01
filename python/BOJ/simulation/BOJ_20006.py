p, m = map(int, input().split())
rooms = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    if len(rooms) == 0:
        rooms.append([(l, n)])
    else:
        for idx in range(len(rooms)):
            if len(rooms[idx]) < m and rooms[idx][0][0] - 10 <= l <= rooms[idx][0][0] + 10:
                rooms[idx].append((l, n))
                break
        else:
            rooms.append([(l, n)])
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(key=lambda x: x[1])
    for level, name in room:
        print(level, name)