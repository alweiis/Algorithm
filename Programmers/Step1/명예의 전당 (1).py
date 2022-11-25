def solution(k, score):
    check, answer = [], []
    for i in score:
        if len(check) < k:
            check.append(i)
        else:
            if check[-1] < i:
                check.pop()
                check.append(i)
        check.sort(reverse=True)
        answer.append(check[-1])
    return answer