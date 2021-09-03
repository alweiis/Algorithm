def check_grade(score):
    if score >= 90:
        answer = 'A'
    elif score >= 80:
        answer = 'B'
    elif score >= 70:
        answer = 'C'
    elif score >= 50:
        answer = 'D'
    else:
        answer = 'F'
    return answer

def solution(scores):
    new_scores = list(map(list, zip(*scores)))
    grade = []
    for i, nums in enumerate(new_scores):
        chk_num = nums[i]
        num = len(new_scores[i])
        if (chk_num == max(nums) or chk_num == min(nums)) and nums.count(chk_num) == 1:
            nums.remove(chk_num)
            num -= 1
        total = sum(nums)
        avg = total / num
        grade.append(check_grade(avg))
    answer = ''.join(grade)
    return answer


