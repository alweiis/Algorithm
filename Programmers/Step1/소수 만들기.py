def solution(nums):
    answer = 0
    length = len(nums)
    sum_lst = []
    for i in range(0, length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                sum_val = nums[i] + nums[j] + nums[k]
                sum_lst.append(sum_val)
    for val in sum_lst:
        cnt_tmp = 0
        for ele in range(1, val + 1):
            if val % ele == 0:
                cnt_tmp += 1
        if cnt_tmp == 2:
            answer += 1
    return answer