n, a, b = map(int, input().split())
arr = [0] * n
arr[a - 1], arr[b - 1] = a, b
game = 1
while True:
    length = len(arr)
    tmp = []
    for i in range(1, length, 2):
        if a not in arr[i - 1:i + 1] and b not in arr[i - 1:i + 1]:
            tmp.append(arr[i])
        elif a in arr[i - 1:i + 1] and b in arr[i - 1:i + 1]:
            print(game)
            exit()
        elif a in arr[i - 1:i + 1]:
            tmp.append(a)
        elif b in arr[i - 1:i + 1]:
            tmp.append(b)
    if length % 2 == 1:
        tmp.append(arr[-1])
    game += 1
    arr.clear()
    arr.extend(tmp)