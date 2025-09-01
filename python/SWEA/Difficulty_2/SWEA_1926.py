n = int(input())
arr = []
for i in range(1, n + 1):
    num = str(i)
    tmp = 0
    for c in num:
        if c in {'3', '6', '9'}:
            tmp += 1
    if tmp == 0:
        arr.append(num)
    else:
        arr.append('-' * tmp)
print(*arr)