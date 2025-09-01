import sys
input = sys.stdin.readline

N, X = map(int, input().split())
records = list(map(int, input().split()))
if max(records) == 0:
    print('SAD')
else:
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + records[i]
    result = []
    for i in range(X, N + 1):
        result.append(prefix_sum[i] - prefix_sum[i - X])
    print(max(result))
    print(result.count(max(result)))