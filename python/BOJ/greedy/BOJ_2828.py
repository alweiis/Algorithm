n, m = map(int, input().split())
start, end = 1, m
count = 0
for _ in range(int(input())):
    x = int(input())
    if x > end:
        count += x - end
        start += x - end
        end = x
    elif x < start:
        count += start - x
        end -= start - x
        start = x
print(count)