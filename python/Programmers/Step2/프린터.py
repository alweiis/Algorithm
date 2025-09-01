def solution(priorities, location):
    check_arr = [0] * len(priorities)
    check_arr[location] = 1
    print_cnt = 0
    while True:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            check_arr.append(check_arr.pop(0))
        else:
            print_cnt += 1
            priorities.pop(0)
            if check_arr.pop(0) == 1:
                return print_cnt