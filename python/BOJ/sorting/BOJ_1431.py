n = int(input())
arr = []
for _ in range(n):
    serial = input()
    length = len(serial)
    number = 0
    for c in serial:
        if c.isnumeric():
            number += int(c)
    arr.append((length, number, serial))
arr.sort(key=lambda x:(x[0], x[1], x[2]))
for x in arr:
    print(x[2])