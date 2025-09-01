from sys import stdin
while True:
    nums = list(map(int, stdin.readline().split()))
    nums.sort()
    if nums[0] == 0:
        break
    diagonal = nums[2] ** 2
    total = (nums[0] ** 2) + (nums[1] ** 2)
    if diagonal == total:
        print('right')
    else:
        print('wrong')