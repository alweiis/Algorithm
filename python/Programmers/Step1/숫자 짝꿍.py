def solution(X, Y):
    answer = ''
    nums = [str(i) for i in range(0, 10)]
    dict_x, dict_y = {}, {}
    for num in nums:
        dict_x[num] = X.count(num)
        dict_y[num] = Y.count(num)
    for num in nums:
        common_count = min(dict_x[num], dict_y[num])
        answer += (num * common_count)
    answer = ''.join(sorted(answer, reverse=True))
    if not answer:
        answer = '-1'
    if answer[0] == answer[-1] == '0':
        answer = '0'
    return answer