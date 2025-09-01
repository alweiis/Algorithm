n = int(input())
m = int(input())
numbers = list(map(int, input().split()))

record = dict()
frame = set()
for idx, num in enumerate(numbers, start=1):
    if num in frame:
        record[num][0] += 1
    else:
        if len(frame) < n:
            frame.add(num)
            record[num] = [1, idx]
        else:
            del_list = sorted(record.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del record[del_key]
            frame.remove(del_key)
            frame.add(num)
            record[num] = [1, idx]
frame = sorted(frame)
print(*frame)