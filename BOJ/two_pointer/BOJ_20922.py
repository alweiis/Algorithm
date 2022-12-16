from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
left, right = 0, 0
check = defaultdict(int)
while right < n:
    if check[arr[right]] < k:
        check[arr[right]] += 1
        right += 1
    else:
        check[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)