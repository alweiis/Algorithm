def solution(s):
    num_dic = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
               '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    if s.isdigit():
        return int(s)
    for k, v in num_dic.items():
        if v in s:
            s = s.replace(v, k)
    return int(s)
