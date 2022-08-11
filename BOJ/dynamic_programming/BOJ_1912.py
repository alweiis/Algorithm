n = int(input())
arr = list(map(int, input().split()))
answer, tmp = arr[0], arr[0]
for i in range(1, n):
    if arr[i] < 0:
        if answer < arr[i]:
            answer = arr[i]
            continue
        if abs(arr[i]) < tmp:
            tmp += arr[i]
        else:
            tmp = 0
    else:
        if tmp < 0:
            tmp = arr[i]
        else:
            tmp += arr[i]
        answer = max(answer, tmp)
print(answer)