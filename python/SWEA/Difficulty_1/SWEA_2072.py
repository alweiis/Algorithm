T = int(input())
for i in range(1, T + 1):
    nums = list(map(int, input().split()))
    nums = [val for val in nums if val % 2 == 1]
    print('#{} {}'.format(i, sum(nums)))