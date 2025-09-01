num = int(input())
nums = list()
for n in range(1, num + 1):
    _sum = n + sum([int(i) for i in str(n)])
    if _sum == num:
        nums.append(n)
if nums:
    print(min(nums))
else:
    print(0)