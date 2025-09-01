t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor_num = n % h
    if floor_num == 0:
        room_num = (h * 100) + (n // h)
    else:
        room_num = floor_num * 100 + (n // h + 1)
    print(room_num)
