n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
left, right = 0, 0
while True:
    if right >= n:
        break
    result = sum(arr[left:right+1])
    if result == m:
        count += 1
        left += 1
    elif result > m:
        left += 1
    elif result < m:
        right += 1
print(count)