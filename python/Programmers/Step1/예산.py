def solution(d, budget):
    d_sum = 0
    cnt = 0
    while d_sum < budget:
        if len(d) == 0:
            break
        d_sum += min(d)
        d.remove(min(d))
        if d_sum > budget:
            break
        cnt += 1
    return cnt
