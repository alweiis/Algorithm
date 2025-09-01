N, M = map(int, input().split())
arr = [-1] + list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
    elif a == 2:
        for i in range(b, c+1):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    elif a == 3:
        arr[b:c+1] = [0] * (c-b+1)
    else:
        arr[b:c+1] = [1] * (c-b+1)
print(*arr[1:])