def solution(s):
    tmp_lst = []
    if s[0] == ')':
        return False
    for val in s:
        if val == '(':
            tmp_lst.append(val)
        elif val == ')' and len(tmp_lst) == 0:
            return False
        else:
            tmp_lst.pop()
    if len(tmp_lst) > 0:
        return False
    return True
