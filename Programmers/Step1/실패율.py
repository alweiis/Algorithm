def solution(N, stages):
    fail_rate, result = [], []
    player = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        if not count:
            rate = 0
        else:
            rate = count / player
        fail_rate.append((rate, i))
        player -= count
    fail_rate.sort(key=lambda x: (-x[0], x[1]))
    result = [stage for _, stage in fail_rate]
    return result