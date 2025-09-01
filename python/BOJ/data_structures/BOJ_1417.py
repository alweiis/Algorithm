n = int(input())
check = int(input())
count = 0
arr = sorted([int(input()) for _ in range(n-1)], reverse=True)
if arr:
    while check <= arr[0]:
        tmp = arr[0]
        arr = arr[1:]
        arr.append(tmp - 1)
        arr.sort(reverse=True)
        check += 1
        count += 1
print(count)