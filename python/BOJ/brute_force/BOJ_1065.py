def check_number(num):
    if num < 100:
        return num
    else:
        hansu_cnt = 99
        for chk_num in range(100, num + 1):
            nums = list(map(int, str(chk_num)))
            if nums[2] - nums[1] == nums[1] - nums[0]:
                hansu_cnt += 1
    return hansu_cnt

n = int(input())
print(check_number(n))