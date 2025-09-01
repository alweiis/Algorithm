T = int(input())
for i in range(1, T + 1):
    nums = list(map(int, input().split()))
    print('#{} {}'.format(i, max(nums)))