def solution(priorities, location):
    sequence = 0
    dummy_lst = [0] * len(priorities)
    dummy_lst[location] = 1
    while len(priorities) != 1:
        first_val = priorities[0]
        max_val = max(priorities[1:])
        if first_val >= max_val:
            priorities.pop(0)
            sequence += 1
            if dummy_lst.pop(0) == 1:
                return sequence
        else:
            p_val = priorities.pop(0)
            d_val = dummy_lst.pop(0)
            priorities.append(p_val)
            dummy_lst.append(d_val)
    else:
        sequence += 1
        return sequence
