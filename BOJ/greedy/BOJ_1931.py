import sys
input = sys.stdin.readline
n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: (x[0], x[1]))
tmp_start, tmp_end = schedule[0][0], schedule[0][1]
count = 1
for start, end in schedule[1:]:
    if tmp_end > end:
        tmp_start = start
        tmp_end = end
    elif tmp_end <= start:
        tmp_start = start
        tmp_end = end
        count += 1
print(count)