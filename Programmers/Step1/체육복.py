def solution(n, lost, reserve):
    common = list(set(lost) & set(reserve))
    lost = sorted(set(lost) - set(common))
    reserve = sorted(set(reserve) - set(common))
    can_attend_num = n - len(lost)
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            can_attend_num += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            can_attend_num += 1
    return can_attend_num