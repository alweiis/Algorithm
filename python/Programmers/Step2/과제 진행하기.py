def convert(start):
    h, m = map(int, start.split(":"))
    return h * 60 + m

def solution(plans):
    plans = [(name, convert(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1])
    answer, stack = [], []

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        if i == len(plans) - 1:
            answer.append(name)
            break
        n_name, n_start, n_playtime = plans[i+1]
        if start + playtime <= n_start:
            answer.append(name)
            tmp_time = n_start - (start + playtime)
            while tmp_time != 0 and stack:
                r_name, remain = stack.pop()
                if tmp_time >= remain:
                    answer.append(r_name)
                    tmp_time -= remain
                else:
                    stack.append([r_name, remain - tmp_time])
                    tmp_time = 0
        else:
            remain = playtime - (n_start - start)
            stack.append([name, remain])
    while stack:
        name, _ = stack.pop()
        answer.append(name)
    return answer