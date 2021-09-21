n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
count = 0
start, end = 0, n - 1
while start < end:
    sum_value = arr[start] + arr[end]
    if sum_value == x:
        count += 1
        start += 1
    elif sum_value > x:
        end -= 1
    elif sum_value < x:
        start += 1
print(count)