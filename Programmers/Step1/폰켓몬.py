def solution(nums):
    available_num = len(nums) / 2
    chk_lst = list(set(nums))
    chk_nums = len(chk_lst)
    if chk_nums > available_num:
        return available_num
    else:
        return chk_nums