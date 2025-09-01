def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    max_w = sizes[0][0]
    max_h = sizes[0][1]
    for i in range(len(sizes)):
        if max_w < sizes[i][0]:
            max_w = sizes[i][0]
        if max_h < sizes[i][1]:
            max_h = sizes[i][1]
    answer = max_w * max_h
    return answer