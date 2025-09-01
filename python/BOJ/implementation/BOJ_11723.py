from sys import stdin

s = set()
r = {x for x in range(1, 20 + 1)}
m = int(stdin.readline())
num = 0
for _ in range(m):
    order = stdin.readline().split()
    if len(order) == 2:
        command = order[0]
        num = int(order[1])
    else:
        command = order[0]

    if command == 'add':
        s.add(num)
    elif command == 'remove':
        s.discard(num)
    elif command == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif command == 'empty':
        s.clear()
    elif command == 'all':
        s = r