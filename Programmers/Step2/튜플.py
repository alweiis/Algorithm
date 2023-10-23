def solution(s):
    answer = []
    s1 = s[1:len(s)-1]
    tmp_str = ''
    tmp_arr, check_arr = [], []
    for c in s1:
        if c.isdigit():
            tmp_str += c
        elif c == ',' and tmp_str != '':
            tmp_arr.append(tmp_str)
            tmp_str = ''
        elif c == '}' and tmp_str != '':
            tmp_arr.append(tmp_str)
            tmp_str = ''
            check_arr.append(tmp_arr)
            tmp_arr = []
    check_arr.sort(key=lambda x:len(x))
    check_set = set()
    for tmp in check_arr:
        for x in tmp:
            if x not in check_set:
                check_set.add(x)
                answer.append(int(x))
    return answer