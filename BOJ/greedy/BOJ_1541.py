s = input()
nums = s.split('-')
if '+' in nums[0]:
    positive_nums = list(map(int, nums[0].split('+')))
    ans = sum(positive_nums)
else:
    ans = int(nums[0])
for i in range(1, len(nums)):
    if '+' in nums[i]:
        negative_nums = list(map(int, nums[i].split('+')))
        ans -= sum(negative_nums)
    else:
        ans -= int(nums[i])
print(ans)