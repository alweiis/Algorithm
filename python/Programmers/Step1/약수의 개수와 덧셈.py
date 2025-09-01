def solution(left, right):
    num_lst = list(range(left, right + 1))
    answer = 0
    for num in num_lst:
        chk_tmp = []
        for i in range(1, num + 1):
            if num % i == 0:
                chk_tmp.append(i)
        if len(chk_tmp) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer
