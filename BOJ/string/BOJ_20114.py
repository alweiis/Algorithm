n, h, w = map(int, input().split())
answer = ['?'] * n
for _ in range(h):
    strs = input()
    arr = []
    for i in range(0, n*w, w):
        arr.append(strs[i:i+w])
    for i in range(n):
        if answer[i] != '?':
            continue
        for c in list(arr[i]):
            if c != '?':
                answer[i] = c
print(''.join(answer))