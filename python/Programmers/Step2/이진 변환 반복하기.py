def solution(s):
    calculation_cnt, zero_cnt = 0, 0
    while s != '1':
        zero_cnt += s.count('0')
        s = format(len(s) - s.count('0'), 'b')
        calculation_cnt += 1
    return [calculation_cnt, zero_cnt]