room_num = input()
arr = [0] * 10
for i in range(len(room_num)):
    num = int(room_num[i])
    if num == 6 or num == 9:
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[num] += 1
print(max(arr))