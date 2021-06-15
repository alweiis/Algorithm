def solution(array, commands):
    answer = []
    for idx in commands:
        i = idx[0]
        j = idx[1]
        k = idx[2]
        answer_tmp = sorted(array[i - 1:j])
        k_num = answer_tmp[k - 1]
        answer.append(k_num)
    return answer
