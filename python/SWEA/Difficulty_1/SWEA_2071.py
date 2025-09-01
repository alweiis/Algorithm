T = int(input())
for i in range(1, T + 1):
    nums = sum(list(map(int, input().split())))
    average = round(nums / 10)
    print('#{} {}'.format(i, average))